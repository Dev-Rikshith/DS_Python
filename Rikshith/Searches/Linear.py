
#ALgorithm: Linear Search
#Time complexity: O(n)
#Space complexity: O(n)

def linear_search(arr, key):
	for i in range(len(arr)):
		if(arr[i] == key):
			print("Element found at", end=" ")
			print(i+1)
			return;
		print("ELement not found")

def main():
    size = int(input("Enter the size of the array:"))
    arr = input()
    l = list(map(int,arr.split(' '))) 
    print(l)
    key = int(input("Enter the element to search"))
    linear_search(l, key)

if __name__ == "__main__":
    main()
