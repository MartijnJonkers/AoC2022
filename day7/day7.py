# build folder/file structure in following format:
#   <folder>
#     _files : files with sizes
#     _size  : size of files and folders combined
#     <subfolders> :
#       _files : files with sizes
#       _size  : size of files and folders combined
#       <subfolders> :
structure = {"/":{"_files":{}, "_size":0}}
cur_ref = structure["/"]                            # points to the current folder
cur_path = [structure["/"]]                         # current path

input = open('day7/input.txt').readlines()
for line in input[1:]:                              # go over all lines (skipping the 'cd /' command)
  l = line.strip().split(' ')                         # parse the line

  if l[0] == "$":                                     # command
    if l[1] == "cd":                                    # change directory
      if l[2] == "..":                                    # path up
        cur_path = cur_path[:-1]                            # go up 1 folder
        cur_ref = cur_path[-1]                              # update folder reference
      else:                                               # path down
        if l[2] not in cur_ref.keys():
          cur_ref[l[2]] = {"_files":{}, "_size":0}            # add new subdir, no files yet
        cur_ref = cur_ref[l[2]]                             # update folder reference
        cur_path.append( cur_ref )                          # go one folder deeper

  elif l[0] == "dir":                                 # is sub dir
    if l[1] not in cur_ref.keys():
      cur_ref[l[1]] = {"_files":{}, "_size":0}          # add new subdir, no files yet

  else:                                               # anything else is a file
    if l[1] not in cur_ref["_files"].keys():
      cur_ref["_files"][l[1]] = int(l[0])              # new file
    cp = cur_path                                        # start computing sizes at current folder
    while len(cp) > 0:                                   # go over all folders from cp up to the root
      cp[-1]["_size"] = sum(cp[-1]["_files"].values())     # compute size of files
      for key in cp[-1]:                                   # add size of all subfolders
        if key != "_files" and key != "_size":
          cp[-1]["_size"] += cp[-1][key]["_size"]
      cp = cp[:-1]                                         # go one folder up in the current path

# build a list with folder sizes
folders = {}
def build_folderlist(structure, prefix = ""):
  for folder in structure:                                          # go over all items in current file
    if folder != "_files" and folder != "_size":                      # skip the files and size helpers
      folders[prefix+"/"+folder] = structure[folder]["_size"]           # store size of the folder
      build_folderlist(structure[folder], prefix+"/"+folder)            # move into the subfolder
build_folderlist(structure)

# part 1: sum of all folders < 100000 in size
part1 = 0
for folder in folders:
  if folders[folder] <= 100000:
    part1 += folders[folder]
print(part1)

# part 2: folder with smallest size over 'needed_space'
needed_space = 30000000 - (70000000 - structure["/"]["_size"])
part2 = 30000000
for folder in folders:
  if folders[folder] <= part2 and folders[folder] >= needed_space :
    part2 = folders[folder]
print(part2)
