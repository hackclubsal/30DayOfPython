monthDict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

month=int(input('Enter month encoded as 1(january) to 12(December):- '))
year=int(input('If you want to check for Leap year entet Year other wise enter 0:- '))
if(((year%100) and not(year%4)) or not(year%400)):
    monthDict[2]=29

if(month>=1 and month<=12):
    print(monthDict[month])
else:
    print('You have Entered between range 1 to 12,Try again 👍')



























#using hash
"""
class HashTable:
  
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    # Insert values into hash map
    def set_val(self, key, val):
        
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
  
    # Return searched value with specific key
    def get_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
  
    # Remove a value with specific key
    
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  

monthList=[31,28,31,30,31,30,31,31,30,31,30,31]
month=int(input('Enter month for which you want days 1 (january) to 12 (December):- '))

leap = int(input("If you want don't to check days in Month in Leap Year enter 0 other wise enter Year for which you want to check days:- "))

if(leap):
    if(((leap%100) and not(leap%4)) or not(leap%400)):
        monthList[1]=29

  
hash_table = HashTable(12)

for i in range(12):
    hash_table.set_val(i+1,monthList[i])
'''    
# insert some values
hash_table.set_val(1, 31)
print(hash_table)
print()
  
hash_table.set_val(2, )
print(hash_table)
print()
'''  

        

# search/access a record with key
print(hash_table.get_val(month))
print()
'''  
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)
'''
"""