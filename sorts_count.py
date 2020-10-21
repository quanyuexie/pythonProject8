# Author: Quanyue Xie
# Date: 10/21/2020
# Description： count the number of change and compare in
#bubble sort and insertion sort, and think the difference between
#different kind of list


#if the numbers in the list are almost sequential
#the change number will be smaller, but the compare number will be the same

a_list = [1,6,5,3,8,4]
def bubble_count(a_list):
  """
  Sorts a_list in ascending order
  """
  compare_num= 0
  change_num = 0
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp
        #everytime if num changed, there should be add 1
        change_num += 1
      #everytime if there is a comparison, add 1
      compare_num += 1
  #return a tuple of the two values
  return (compare_num,change_num)

def insertion_count(a_list):
  change_number = 0
  compare_number = 0
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
      # everytime if num changed, there should be add 1
      change_number += 1
    # everytime if there is a comparison, add 1
    compare_number += 1
    a_list[pos + 1] = value
  # return a tuple of the two values
  return (compare_number, change_number)




