from time import time, sleep
from typing import Callable
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from dateutil.parser import parse
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from requests import get, Response


class GbBlogParse:
    BASE_URL = 'https://gb.ru'
    DELAY = 1.0
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) "
                      "Gecko/20100101 Firefox/88.0"
    }

    def __init__(self, db_connection):
        self.db = db_connection
        self.next_request_time = time()
        self.done_urls = []
        self.tasks = []
        self.current_page_number = 0
        self.add_next_page_to_tasks()

    def get_response(self, url):
        self.wait_for_next_request_time()

        response = get(url, headers=self.HEADERS)
        print(f"RESPONSE: {response.url}")

        if 200 <= response.status_code < 300:
            return response
        else:
            raise Exception(f"Bad response from {url}")

    def wait_for_next_request_time(self):
        if self.next_request_time > time():
            sleep(self.next_request_time - time())
        self.next_request_time = time() + self.DELAY

    def get_task(self, url: str, callback: Callable) -> Callable:
        def task():
            response = self.get_response(url)
            return callback(response)

        return task

    def tasks_creator(self, urls: list, callback: Callable):
        for url in urls:
            if url in self.done_urls:
                continue

            self.tasks.append(
                self.get_task(url, callback)
            )
            self.done_urls.append(url)

    def run(self):
        while len(self.tasks) > 0:
            task = self.tasks.pop(0)
            task()

    @classmethod
    def find_post_urls(cls, page: BeautifulSoup) -> [str]:
        return [
            urljoin(cls.BASE_URL, post.a['href'])
            for post in page.find_all('div', 'post-item') if
            post.a and post.a.has_attr('href')
        ]

    def parse_feed(self, response: Response):
        soup = BeautifulSoup(response.text, 'lxml')
        post_urls = self.find_post_urls(soup)

        if len(post_urls) == 0:
            return

        self.tasks_creator(post_urls, self.parse_post)
        self.add_next_page_to_tasks()

    def current_page_url(self):
        return urljoin(self.BASE_URL, f"/posts?page={self.current_page_number}")

    def add_next_page_to_tasks(self):
        self.current_page_number += 1
        self.tasks_creator([self.current_page_url()], self.parse_feed)

    def parse_post(self, response: Response):
        soup = BeautifulSoup(response.text, 'lxml')
        author_name_tag = soup.find('div', {"itemprop": "author"})
        time_tag = soup.find('time', {'itemprop': 'datePublished'})
        published_at = parse(time_tag['datetime'])
        post_id = soup.find("comments").get("commentable-id")

        data = {
            "post_data": {
                "title": soup.find('meta', {'property': 'og:title'})['content'],
                "url": response.url,
                "id": post_id,
                "image_url": soup.find('meta', {'property': 'og:image'})['content'],
                "published_at": published_at
            },
            "author_data": {
                "url": urljoin(response.url, author_name_tag.parent["href"]),
                "name": author_name_tag.text,
            },
            "comments_data": self.get_comments(post_id)
        }
        self.save(data)

    def save(self, data: dict):
        collection = self.db["gb_blog_parse"]
        query = {"post_data.id": data["post_data"]["id"]}
        update = {"$set": data}
        collection.update_one(query, update, True)

    def get_comments(self, post_id):
        api_path = f"/api/v2/comments?commentable_type=Post&commentable_id={post_id}&order=desc"
        api_url = urljoin(self.BASE_URL, api_path)
        response = self.get_response(api_url)
        return [
            {
                'author': comment['comment']['user']['full_name'],
                'text': comment['comment']['body']
            }
            for comment in response.json()
        ]


if __name__ == '__main__':
    client_db = MongoClient("mongodb://localhost:27017")

    try:
        client_db.server_info()
    except ConnectionFailure:
        print("Unable to connect to MongoDB")
        exit(1)

    db = client_db["gb_parse_blog"]
    parser = GbBlogParse(db)
    parser.run()
