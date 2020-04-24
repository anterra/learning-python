points = [{"x": 2, "y": 3},
          {"x": 4, "y": 1}]
points.sort(key=lambda i: i["y"]) #.sort takes a key parameter which determines how the list is sorted
    #lamba is used to create a new function rather than writing a separate def block for a function
    #that will get used only in one place
print(points)
