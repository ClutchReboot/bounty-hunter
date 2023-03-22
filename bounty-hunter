#!/usr/bin/env python3
import argparse
import os
import shutil

from utils import tools


class BountyHunter:
    def __init__(self, name: str, ip: str):
        self.name = tools.sanitize_file_name(file=name)
        self.ip = tools.sanitize_ipv4(ip=ip)

        self.home = os.environ['HOME']
        self.cwd = os.getcwd()

        self.source_directory = os.path.abspath(os.path.dirname(__file__))
        self.destination_directory = os.path.abspath(self.name)

        self.md_files = list()

    def copy_dir_template(self):
        """
        Copy 'dir_template' to the new destination.
        """

        dir_template_path = os.path.abspath(f"{self.source_directory}/dir_template")
        shutil.copytree(dir_template_path, self.destination_directory)
        return f"The 'dir_template' has successful been copied to '{self.destination_directory}'."

    def find_md_files(self):
        for root, dirs, files in os.walk(self.destination_directory):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                if file_extension == '.md':
                    self.md_files.append(f"{root}/{file}")

        return self.md_files

    def replace_template_variables(self):
        for file in self.md_files:
            data = tools.read_file(file=file)
            data = data.replace("{{TARGET}}", f"{self.name.lower()}.htb")
            data = data.replace("{{TARGET_IP}}", f"{self.ip}")
            tools.write_file(file=file, data=data)

    def main(self):
        self.copy_dir_template()
        self.find_md_files()
        self.replace_template_variables()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Setup a workspace specifically for HTB.')
    parser.add_argument('-n', '--name', help='Name of HTB machine.', required=True)
    parser.add_argument('-i', '--ip', help='IP Address of HTB machine.', required=True)

    args = parser.parse_args()

    x = BountyHunter(name=args.name, ip=args.ip)
    x.main()
