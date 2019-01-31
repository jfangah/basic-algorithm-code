import pandas as pd 
import pprint 

class Classifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None


    def __init__(self,filename=None, class_attr=None ):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.class_attr = class_attr

    '''
        probability(class) =    How many  times it appears in cloumn
                             __________________________________________
                                  count of all class attribute
    '''
    def calculate_priori(self):
        class_values = list(set(self.data[self.class_attr]))
        class_data =  list(self.data[self.class_attr])
        # Your Code1
        for i in class_values:
            sum1=0
            for j in class_data:
                if i==j:
                    sum1=sum1+1
            values=sum1*1.0/len(class_data)
            self.priori[i]=values
        print( "Priori Values: ", self.priori)

    '''
        Here we calculate the individual probabilites 
        P(outcome|evidence) =   P(Likelihood of Evidence) x Prior prob of outcome
                               ___________________________________________
                                                    P(Evidence)
    '''
    def get_cp(self, attr, attr_type, class_value):
                    #(age,  <=30,      no)
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])
        total =1.0
        #Your Code2
        sum1=0
        sum2=0
        for i in range(len(class_data)):
            if class_data[i]==class_value:
                sum1=sum1+1
                if data_attr[i]==attr_type:
                    sum2=sum2+1
        return total*sum2/sum1
        

    '''
        Here we calculate Likelihood of Evidence and multiple all individual probabilities with priori
        (Outcome|Multiple Evidence) = P(Evidence1|Outcome) x P(Evidence2|outcome) x ... x P(EvidenceN|outcome) x P(Outcome)
        scaled by P(Multiple Evidence)
    '''
    def calculate_conditional_probabilities(self, hypothesis):
        for i in self.priori:
            self.cp[i] = {}
            for j in hypothesis:
                self.cp[i].update({ hypothesis[j]: self.get_cp(j, hypothesis[j], i)})
        print ("\nCalculated Conditional Probabilities: \n")
        pprint.pprint(self.cp)

    def classify(self):
        print ("Result: ")
        for i in self.cp:
            print( i, " ==> ", reduce(lambda x, y: x*y, self.cp[i].values())*self.priori[i])

if __name__ == "__main__":
    c = Classifier(filename="dataset.csv", class_attr="Buys_Computer" )
    c.calculate_priori()
    c.hypothesis = {"Age":'<=30', "Income":'medium', "Student":'yes' , "Credit_Rating":'fair'}
    c.calculate_conditional_probabilities(c.hypothesis)
    # Your Code3
    c.classify()
