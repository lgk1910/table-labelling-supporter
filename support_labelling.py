# Arguments
table_infos = [
    {
        'row_num': 8,
        'col_num': 3,
    },
    {
        'row_num': 6,
        'col_num': 2,
    },
]

line_id = 47
label_file_path = 'part_002\Label.txt'
merged_cells = [
    [
    ],
    [
    ],
]
added_merged_cells = [[] for lst in merged_cells]

# BODY
# Read input_string
with open(label_file_path, 'r') as f:
    file_content = f.read()
    lines = file_content.splitlines()
    
input_str = ''
input_str_copy = lines[line_id].split('\t')[-1]
input_str = lines[line_id].split('\t')[-1]
# with open('input_tmp.txt', 'r') as f:
#     input_str = f.read()

# Preprocess input string
input_str = input_str.replace('false', 'False').replace('true', 'True')
    
# Start processing
def belong_to_merged_cell(input_cell, merged_cells):
    for merge_cell in merged_cells:
        if input_cell[0] >= merge_cell[0]\
            and input_cell[1] <= merge_cell[1]\
                and input_cell[2] >= merge_cell[2]\
                    and input_cell[3] <= merge_cell[3]:
            return True, merge_cell
    return False, None
        
label_lsts = []
for table_id, table_info in enumerate(table_infos):
    row_num = table_info['row_num']
    col_num = table_info['col_num']
    label_lst = []
    i = 0
    j = 0
    while i < row_num:
        while j < col_num:
            belong_to_mc, mc = belong_to_merged_cell([i,i,j,j], merged_cells[table_id])
            if not belong_to_mc:
                label_lst.append(str([i,i,j,j]).replace(' ', ''))
            else:
                if mc not in added_merged_cells[table_id]:
                    label_lst.append(str(mc).replace(' ', ''))
                    added_merged_cells[table_id].append(mc)
                j = mc[3]
            j += 1
        i += 1
        j = 0
    label_lst.append("TEMPORARY")
    label_lsts += label_lst
    
print(f'label_lsts len: {len(label_lsts)}')
# print(f'label_lsts: {label_lsts}')
input_lst = eval(input_str)
print(f'input_lst len: {len(input_lst)}')
# print(f'input_lst: {input_lst}')

for i in range(len(label_lsts)):
    try:
        input_lst[i]["transcription"] = label_lsts[i]
    except Exception as E:
        print(f'{E} at {i}')
    

output_str = str(input_lst)
# Postprocess output string
output_str = output_str.replace('False', 'false').replace('True', 'true')
output_str = output_str.replace('\'', '\"')
file_content = file_content.replace(input_str_copy, output_str)
with open(label_file_path, 'w') as f:
    f.write(file_content)


