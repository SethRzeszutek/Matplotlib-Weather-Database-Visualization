'''
 Name of file: Rzeszutek_2
 Purpose:Graph

 Author: Seth Rzeszutek

 Date Created: Sept. 18, 2017

'''
import matplotlib.pyplot as pyplot

def number_check(value):
    '''
    Purpose: Checks if value is a number
    :param: value
    :return: True or False
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

def plotTemps(fileName, userBirthMonth):
    '''
    Purpose: Plots Graphs
    :param:fileName
    :param:userBirthMonth
    :return:
    '''
    ######Declaring#######
    temp = []
    rain = []
    datetemp =[]
    datetemp2 =[]
    daterain = []
    daterain2 =[]
    tempAvg=[]
    figure = pyplot.figure()
    axis = figure.add_subplot(111)                                                  #getting ready for plotting graphs

    userBirthMonth=str(userBirthMonth)                                              #formatting the user birth month
    userBirthMonth ='0'+userBirthMonth

    file = open(fileName)                                                           #open file
    for line in file:
        column = line.split(',')
        monthColumn = column[5][5:7]
        dayPos = column[5][8:10]
        yearPos = column[5][0:4]
        if(monthColumn == userBirthMonth):                                             #tests for user birth month
            if(number_check(column[26])):
                temp.append(float(column[26]))
                datetemp.append((int(dayPos), float(column[26]), int(yearPos)))     #Birth month temperature through all years
            if(number_check(column[38])):
                rain.append(float(column[38]))
                daterain.append((int(dayPos), float(column[38]), int(yearPos)))     #Birth month rainfball through all years
        if(number_check(column[26])):
            datetemp2.append((float(column[26]), int(yearPos)))                     #total temperature through all years
        if(number_check(column[38])):
            daterain2.append((float(column[38]), int(yearPos)))                     #total rainfall through all years
    file.close()                                                                    #close file

    ######Separating into lists#######
    date1, temp, year1 = zip(*datetemp)
    date2, rain, year2 = zip(*daterain)

    temp2, year3 = zip(*datetemp2)
    rain2, year4 = zip(*daterain2)



    amount = 0
    x=0
    totalTemp=0
    z = datetemp2[0][1]
    yearAvg = [datetemp2[0][1]]
    for i in datetemp2:                                                             #calculates average temperature for each year
        if i[1]==z:
            totalTemp+=temp2[x]
            amount +=1
        else:                                                                       #changes to next year
            yearAvg += [i[1]]
            tempAvg += [totalTemp/amount]
            z = i[1]
            totalTemp=0
            amount=0
        x+=1
    tempAvg+=[totalTemp/amount]

    amount = 0
    x=0
    totalRain=0
    z = daterain2[0][1]
    yearAvg2 = [daterain2[0][1]]
    rainAvg = []
    for i in daterain2:                                                             #calculates average rainfall for each year
        if i[1]==z:
            totalRain+=rain2[x]
            amount +=1
        else:                                                                       #changes to next year
            yearAvg2 += [i[1]]
            rainAvg += [totalRain/amount]
            z = i[1]
            totalRain=0
            amount=0
        x+=1
    rainAvg+=[totalRain/amount]

    axis.set_title('Monthly Temperature')
    axis.set_xlabel('Years')
    axis.set_ylabel('Temps')
    pyplot.plot(year1, temp)                                                        #graphs Monthly Temperatures
    pyplot.show()
    axis.clear()

    axis.set_title('Monthly Rainfall')
    axis.set_xlabel('Years')
    axis.set_ylabel('Rain')
    pyplot.plot(year2, rain)                                                        #graphs Monthly Rainfall
    pyplot.show()
    axis.clear()

    axis.set_title('Average Yearly Temperature')
    axis.set_xlabel('Years')
    axis.set_ylabel('Average Temperature')
    pyplot.plot(yearAvg, tempAvg)                                                   #graphs yearly average Temperatures
    pyplot.show()
    axis.clear()


    axis.set_title('Average Yearly Rainfall')
    axis.set_xlabel('Years')
    axis.set_ylabel('Average Rainfall')
    pyplot.plot(yearAvg, rainAvg)                                                   #graphs yearly average rainfall
    pyplot.show()
    axis.clear()

def main():
    '''
    Purpose: Perform main
    :param:
    :return:
    '''
    fileName = '/Users/SethRzeszutek/Downloads/assignment02_data/1066025.csv'       #file path
    userBirthMonth = 3                                                              #user birth month
    plotTemps(fileName, userBirthMonth)


# main function call
if __name__ == '__main__':
    main()
