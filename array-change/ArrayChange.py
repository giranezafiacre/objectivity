def array_changes(original, updated):
    original_set = set(original)
    updated_set = set(updated)
    new_elements = updated_set - original_set
    removed_elements = original_set - updated_set
    return list(new_elements), list(removed_elements)

originalArray=[1,3,4,6]
updatedArray=[5,3,2,1]
newElement,removedElement=array_changes(originalArray,updatedArray)
print('original Array input:',originalArray)
print('updated Array input:',updatedArray)
print('new elements:',newElement)
print('removed elements:',removedElement)