import pathInit #Search in the right pathsfrom tasks import Taskfrom filetypes import Taskpaperimport osif __name__ == '__main__':	print('Reading from {0}'.format(os.path.join('filetypes', 'samples', 'sample_taskpaper.taskpaper')))	tasklist = Taskpaper.readFile(os.path.join('filetypes', 'samples', 'sample_taskpaper.taskpaper'))	print(Taskpaper.getFileString(tasklist) + '\n')