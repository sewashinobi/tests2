import sys

def compress_string(input_str):
	compressed_output_str = ""
	s_index = 0
	while s_index < len(input_str):
		count = 1
		while s_index < (len(input_str) - 1) and input_str[s_index] == input_str[s_index + 1]:
			s_index += 1
			count += 1
		compressed_output_str += input_str[s_index]
		compressed_output_str += str(count)
		s_index += 1
	return compressed_output_str

if __name__ == '__main__':
	input_str = sys.argv[1]
	print compress_string(input_str)
