import textfsm

with open("ip_interface_brief_template.txt") as template_file:
    template = textfsm.TextFSM(template_file)

with open("sample_output.txt") as output_file:
    output_data = output_file.read()

parsed_data = template.ParseText(output_data)

for item in parsed_data:
    print(item)