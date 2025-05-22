import pandas as pd 
import matplotlib.pyplot as plt

class Dashbaord: 
    
    def parse_csv(self): 
        ''' 
        Extract and parse data from the CSV file 
        '''
        
        nsdq_appl = pd.read_csv('HistoricalData_APPL.csv')
        return nsdq_appl
    
    
    def plot(self): 
        ''' 
        plot the extracted data into a graph 

        ----------------------------------------
        x-axis: date 
        y-axis: price 
        '''

        appl_data = self.parse_csv() 
        appl_data['Date'] = pd.to_datetime(appl_data['Date'])

        appl_data = appl_data.sort_values(by = 'Date')

        plt.plot(appl_data['Date'], appl_data['Open'])
        plt.show()


appl_stocks = Dashbaord()
appl_stocks.plot()