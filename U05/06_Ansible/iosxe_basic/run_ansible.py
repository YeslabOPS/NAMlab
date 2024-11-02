import subprocess
import logging
import os

logging.basicConfig(
    filename='log.txt',      # 日志文件名
    filemode='a',            # 追加模式
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
    level=logging.DEBUG       # 日志级别
)

def get_yaml_files(directory):
    yaml_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.yml') or filename.endswith('.yaml'):
            yaml_files.append(os.path.join(directory, filename))
    return yaml_files

def main():
    playbooks = get_yaml_files('.')
    playbooks.sort()
    for playbook in playbooks:
        command = ["ansible-playbook", playbook, "-i", "../inventory/cisco.yaml"]
        result = subprocess.run(command, capture_output=True, text=True)

        # 记录日志
        logging.info(f"[Playbook]: {playbook}")
        logging.info(f"stdout\n:{result.stdout}")
        logging.error(f"stderr\n:{result.stderr}")

main()
