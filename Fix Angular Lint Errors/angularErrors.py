# program to search for and replace given angular warnings
import os, re, itertools, sys
from os.path import join, getsize

def replace(file_path, oldExpr, newExpr):
	edited_files = 0

	# iterate through all sub directories and files
	for root, dirs, files in os.walk(file_path):
		for filename in files:
			if filename.endswith(".ts"): # or filename.endswith(".js"):
				full_path = root + "\\" + filename

				# open file and read in file
				fh = open(full_path, 'r')
				subject = fh.read()
				fh.close()
				# replaces text

				if re.search(oldExpr, subject) is not None:
					# uncomment to prints file being processed
					# print(full_path)
					# replaces old value with new value
					pattern = re.compile(oldExpr)
					result = pattern.sub(newExpr, subject)

					# write replaced text to file
					f_out = open(full_path, 'w')
					f_out.write(result)
					f_out.close()

					# Only iterate if file was edited
					edited_files += 1

	print("Edited %s file(s)" % edited_files)

file_path = "C:\\Temp\\1"

# fix comments without space
# //comment -> // comment
print("\n\rFixing Error: \"Comment must start with a space\"")
oldExpr = r'(?<!\w|:)//(?:(\w))'
newExpr = r'// \1'
replace(file_path, oldExpr, newExpr)

oldExpr = r'../../core/services// models'
newExpr = r'../../core/services/models'
replace(file_path, oldExpr, newExpr)

# fix trailing whitespace
print("\n\rFixing Error: \"Trailing whitespace\"")
oldExpr = r'[ \t]+(\n|\Z)'
newExpr = r'\1'
replace(file_path, oldExpr, newExpr)

# file ends with new line
print("\n\rFixing Error: \"File should end with a newline\"")
oldExpr = r'(?<![\r\n])$(?![\r\n])'
newExpr = r'\r\n'
replace(file_path, oldExpr, newExpr)

# file ends with new line
print("\n\rFixing Error: \"Space indentation expected\"")
oldExpr = r'\t'
newExpr = r'    '
replace(file_path, oldExpr, newExpr)

# fixes missing space
# if(true) -> if (true)
print("\n\rFixing Error: \"Missing whitespace\"")
oldExpr = r'(?:(switch|if|else|\)|}))(\(|\{|else)'
newExpr = r'\1 \2'
replace(file_path, oldExpr, newExpr)

# ex: warning(message: string, title?:string -> warning(message: string, title?: string
print("\n\rFixing Error: \"Missing whitespace\"")
oldExpr = r'(?:(\?):(\w))'
newExpr = r'\1: \2'
replace(file_path, oldExpr, newExpr)

# Type trivially inferred from a literal, remove type annotation
# variable: boolean = true -> variable = true
print("\n\rFixing Error: \"Type boolean trivially inferred from a boolean literal, remove type annotation\"")
oldExpr = r'(?:(\: boolean = )(true|false))'
newExpr = r' = \2'
replace(file_path, oldExpr, newExpr)
# Same as above, but with string
print("\n\rFixing Error: \"Type string trivially inferred from a string literal, remove type annotation\"")
oldExpr = r'(?:(\: string = )(''|""))'
newExpr = r' = \2'
replace(file_path, oldExpr, newExpr)
# Same as above, but with number
print("\n\rFixing Error: \"Type number trivially inferred from a number literal, remove type annotation\"")
oldExpr = r'(?:(\: number = )(\d))'
newExpr = r' = \2'
replace(file_path, oldExpr, newExpr)

# == should be ===
print("\n\rFixing Error: \"== should be ===\"")
oldExpr = r'(?:(^|[^!=])([!=]=)(?!=)( \d| \"| \'| true| false| undefined| this))'
newExpr = r' \2=\3'
replace(file_path, oldExpr, newExpr)


# misplaced 'else'
# }		-> } else
# else	->
print("\n\rFixing Error: \"Misplaced 'else'\"")
oldExpr = r'(?:(?<!// )(})(\n\s*)(else))'  #
newExpr = r'\1 \3'
replace(file_path, oldExpr, newExpr)

# misplaced 'catch'
print("\n\rFixing Error: \"Misplaced 'catch'\"")
oldExpr = r'(?:(?<!// )(})(\n\s*)(catch))'  #
newExpr = r'\1 \3'
replace(file_path, oldExpr, newExpr)

# " should be '
print("\n\rFixing Error: \" \" should be ' \"")
oldExpr = r'(?<!\')(")(?!\')'  #
newExpr = "\'"
replace(file_path, oldExpr, newExpr)

# var should be let
print("\n\rFixing Error: \"Var should be let\"")
oldExpr = r' var '  #
newExpr = " let "
replace(file_path, oldExpr, newExpr)
