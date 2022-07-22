#!/usr/bin/env python3

# [(2,5),(3,6),(5,7)]

input = [[2,5],[3,6],[5,7],[1,3],[2,5]]

def overlaps(t1, vm_list):
  for i in vm_list:
    if t1[1] > i[0] and i[1] > t1[0]:
      print(f"{t1} overlaps with {i}")
      return True
    else:
      print(f"{t1} doesn't overlap with {i}")

def get_vm_count(runs_list):
  vm_list = []
  count = 0
  for i in runs_list:
    if runs_list == 0:
      count = 0
    elif len(runs_list) == 1:
      count = 1
    elif len(vm_list) == 0:
      vm_list.append(i)
    elif overlaps(i,vm_list) == True:
      vm_list.append(i)
      count += 1
  return count


if __name__ == "__main__":
  print(f"input: {input}")
  count = get_vm_count(input)
  print(f"vms needed: {count}")