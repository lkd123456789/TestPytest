import yaml,sys,os
sys.path.append(os.getcwd())
class ReadSearch:
    def read_search(self,filename):
        filepath="D:\\Program Files\\JetBrains\\pycharmProjects\\appium1\data\\"+filename+".yml"
        self.data_list=[]
        with open(filepath,"r",encoding="utf-8")as f:
            self.data=yaml.load(f).get("Search_data")
            for i in self.data.keys():
                self.data_list.append(self.data.get(i).get("text"))
            return self.data_list