#!/usr/bin/env python3

import os

# Get the title from the user input
title = input("Enter the title: ")

# Create the file contents
state_content = f"import 'package:get/get.dart';\n\nclass {title}State{{}}\n"
controller_content = f"import 'package:get/get.dart';\nimport '{title.lower()}_index.dart';\n\nclass {title}Controller extends GetxController{{\n  {title}Controller();\n  final state = {title}State();\n}}\n"
binding_content = f"import 'package:get/get.dart';\nimport '{title.lower()}_index.dart';\n\n\nclass {title}Binding extends Bindings {{\n  @override\n  void dependencies() {{\n    // TODO: implement dependencies\n    Get.put<{title}Controller>({title}Controller());\n  }}\n}}\n"
index_content = f"library {title.lower()}Library;\n\nexport 'controller.dart';\nexport 'state.dart';\nexport 'view.dart';\nexport 'binding.dart';\n"

# Create the files
files = ['state.dart', 'controller.dart', 'binding.dart', f'{title.lower()}_index.dart', 'view.dart']
for filename in files:
    file_content = ''
    if filename == 'state.dart':
        file_content = state_content
    elif filename == 'controller.dart':
        file_content = controller_content
    elif filename == 'binding.dart':
        file_content = binding_content
    elif filename == f'{title.lower()}_index.dart':
        file_content = index_content
    # Add an empty view file
    elif filename == 'view.dart':
        open(filename, 'a').close()
    with open(filename, 'w') as f:
        f.write(file_content.replace('title', title.lower()))

print("Files created successfully!")

