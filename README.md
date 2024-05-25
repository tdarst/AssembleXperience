# Releases
## v0.0.1
- This release is the state of my project at the time of my senior design submission. There are plenty of bugs that still need to be worked on.

## Building the Source Code
- On the right side of the page you should see a release section. This section contains options for compressed source code or the exe:
	- Executable
		- I've automated the build process within the release pipeline for the source code so that in each release there will be an available exe.
	- Building the source code:
		- Download the compressed source code from the release section and extract it
		- Install PyInstaller using: python -m pip install pyinstaller==5.13.2
		- Open the root directory in command line
		- Run the command: pyinstaller --onefile --noconsole --name AssembleXperience.exe Code\runSimulator.py
		- The exe should appear in the root directory.
	- Non-compressed source code:
		- The release branch contains all of the source code for the most recent release version as well as a built executable within. You can simply
		clone this branch if you choose to take this method.

# Design Report Table of Contents
1. [Team name and Project Abstract](/Project_Planning_And_Assignments/Project_Description.md)
2. [Test Plan and Results](/Project_Planning_And_Assignments/Test_Plan_And_Results.pdf)
3. [User Docs](/USER_DOCS.md)
4. [Spring Final PPT Presentation](https://docs.google.com/presentation/d/1Zhb0sGaYNVrJPqnTdKtY5an3Z8EAIc17fDHHG__onvo/edit?usp=sharing)
5. [Final Expo Poster](/Project_Planning_And_Assignments/AssembleXperience_Poster.pdf)
6. Self-Assessments
	1. [Fall Self-Assessment](https://mailuc-my.sharepoint.com/:w:/g/personal/darsttd_mail_uc_edu/EQSV9a1MrPNErPY_alzKcc0B7-XVkzDY66qbFKZjJ19Btw?e=fkD8x8)
	2. [Spring Self-Assesment](/Project_Planning_And_Assignments/Spring_Self_Assessment.pdf)
7. [Summary of Hours and Justification](https://mailuc-my.sharepoint.com/:w:/g/personal/darsttd_mail_uc_edu/EYFDPVLA0A5NuX1DPVdQxyoBi6KpYkyOMZAxe4CxmS4_mQ?e=8CyOkW)