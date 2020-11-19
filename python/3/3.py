def my_func(a, b, c):
  """
  Returns sum of two biggest arguments
  """
  nums = [a, b, c]
  nums.sort
  return sum(nums[0:2])


assert my_func(3, 17, 1) == 20, 'my_func(3, 17, 1) should eq 20'
assert my_func(141, 9, 0) == 150, 'my_func(141, 9, 0) should eq 150'
