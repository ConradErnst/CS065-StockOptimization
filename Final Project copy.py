#
# Final Project
#
#Authors:
#   Conrad Ernst & Matthew Lovelace


def parse_file(filename):
    file = open(filename)
    
    file.readline()
    table = []
    for line in file:
        delimiter =","
        row = line.split(delimiter)
        table.append(row)
    file.close()
    return(table)


def get_Company(row):
    return(row[1])

def get_Symbol(row):
    return(row[2])

def get_Weight(row):
    return(int(row[3]))

def get_Sector(row):
    return(row[4])

def get_Q1(row):
    return(int(row[6]))

def get_Q2(row):
    return(int(row[7]))

def get_Q3(row):
    return(int(row[8]))

def get_Dividend(row):
    return(int(row[9]))

def get_Volatility(row):
    return(int(row[12]))


def filter_by_sector(table, sector):
    filter_list = []
    for row in table:
        if get_Sector(row) == sector:
            filter_list.append(row)
    return(filter_list)  
    
    
def company_information(table, symbol):
    for row in table:
        if get_Symbol(row) == symbol:
            return(row)
    
    
def quarter_results(table):
    for row in table: 
        if get_Q1(row) <= get_Q2(row) <= get_Q3(row):
            score = 1
        else:
            score = 2
    return(score)


def average_dividend(table):
    total_dividend = 0
    num_dividends = 0
    for row in table:
        total_dividend += get_Dividend(row)
        num_dividends += 1
    return(total_dividend/num_dividends)


def average_Volatility(table):
    total_volatility = 0
    num_volatility = 0
    for row in table:
        total_volatility += get_Volatility(row)
        num_volatility += 1
    return(total_volatility/num_volatility)


def long_term_stock(table):
    longterm_best = []
    for row in table:
        if get_Dividend(row) > average_dividend(table) and get_Volatility(row) < average_Volatility(table) and quarter_results(table) == 1:
            longterm_best.append(row[1])
    return(longterm_best)


def short_term_stock(table):
    shortterm_best = []
    for row in table:
        if get_Dividend(row) > average_dividend(table) and get_Volatility(row) >= average_Volatility(table) and quarter_results(table) == 1:
            shortterm_best.append(row[1])
    return(shortterm_best)
        
        
def long_term_stock_low(table):
    longterm_best = []
    for row in table:
        if get_Dividend(row) <= average_dividend(table) and get_Volatility(row) < average_Volatility(table) and quarter_results(table) == 1:
            longterm_best.append(row[1])
    return(longterm_best)


def short_term_stock_low(table):
    shortterm_best = []
    for row in table:
        if get_Dividend(row) <= average_dividend(table) and get_Volatility(row) >= average_Volatility(table) and quarter_results(table) == 1:
            shortterm_best.append(row[1])
    return(shortterm_best)


def highest_dividend(table):
    highest = table[0]
    for row in table:
        if get_Dividend > 0:
            if get_Dividend(row) > get_Dividend(highest):
                highest = row
    return(highest)


def sector_weight(table):
    weight = 0 
    for row in table:   
        weight += get_Weight(row)
        

def sector_compare(table, c, s):
    sector_list = filter_by_sector(table, sector_one)
    sector_list2 = filter_by_sector(table, sector_two)
    if average_dividend(sector_list) > average_dividend(sector_list2):
        print("The sector:", sector_one, "has a higher average dividend yeild than the", sector_two, "sector.")
        print(sector_one, "average dividend yeild:", average_dividend(sector_list))
        print(sector_two, "average dividend yeild:", average_dividend(sector_list2))   
    if average_dividend(sector_list) < average_dividend(sector):
        print("The sector:", sector_two, "has a higher average dividend yeild than the", sector_one, "sector.")
        print(sector_two, "average dividend yeild:", average_dividend(sector_list2))
        print(sector_one, "average dividend yeild:", average_dividend(sector_list))
    if sector_weight(sector_list) > sector_weight(sector_list2):
        print("The sector:", sector_two, "makes up more of the S&P Index than the", sector_one, "sector.")
        print(sector_two, "weight in the S&P Index:", sector_weight(sector_list2))
        print(sector_one, "weight in the S&P Index:", sector_weight(sector_list))
    if sector_weight(sector_list2) > sector_weight(sector_list):
        print("The sector:", sector_one, "makes up more of the S&P Index than the", sector_two, "sector.")
        print(sector_one, "weight in the S&P Index:", sector_weight(sector_list))
        print(sector_two, "weight in the S&P Index:", sector_weight(sector_list2)) 
    print("Companies in the", sector_one, "sector", sector_list)
    print("Companies in the", sector_two, "sector", sector_list2)


def Sector_company_information(table, sector, symbol):
    '''This is to show the comparisons of a certain stock in a sector to the other stocks in that sector''' 
    sector_list = filter_by_sector(table, sector) 
    for row in sector_list:
        if get_symbol(row) == symbol:
            if symbol in long_term_stock(sector_list):
                print("The", symbol, "stock is an excellent long term stock")
                print("The divident yeild of the stock is", get_dividend(row), "which is above average in this sector")
                print("It makes up", get_Weight(row),"% of the entire S&P index and has steady company growth") 
            if symbol in short_term_stock(sector_list):
                print("The", symbol, "stock is an excellent long term stock")
                print("The divident yeild of the stock is", get_dividend(row), "which is above average in this sector")
                print("It makes up", get_Weight(row),"% of the entire S&P index and has steady company growth")
            if symbol in long_term_stock_low(sector_list):
                print("The", symbol, "stock is a decent long term stock")
                print("The divident yeild of the stock is", get_dividend(row), "which is below average in this sector")
                print("It makes up", get_Weight(row),"% of the entire S&P index and has steady company growth")
            if symbol in short_term_stock_low(sector_list):
                print("The", symbol, "stock is a decent long term stock")
                print("The divident yeild of the stock is", get_dividend(row), "which is below average in this sector")
                print("It makes up", get_Weight(row),"% of the entire S&P index and has steady company growth")   
            
            
def main():
    table = parse_file()
    goal = input("What objective of the data set would you like to see, (single company, companies by sectors, or ranking results): ")
    if goal == "single company":
        symbol = input("Input the ticker symbol you would like to see information on: ")
        symbol_list = company_information(table, symbol)
        print(symbol_list)
        
    if goal == "companies by sectors":
        sectors = input("What would you like to know more about, (comparison of sectors or list of companies in a sector): ")
        if sectors == "comparison of sectors":
            sector_one = input("What is the first sector you would like to compare: ")
            sector_two = input("What is the second sector you would like to compare: ")
            print(sector_compare(table, sector_one, sector_two))
        if sectors == "list of companies in a sector":
            sector = input("What sector would you like to look at: ")
            print(filter_by_sector(table, sector))
            sector_2 = input("Would you like to know more about a company in this sector? ")
            if sector_2 == yes or sector_2 == Yes or sector_2 == YES:
                symbol = input("Input the ticker symbol you would like to see information on: ")
                print(Sector_company_information(table, sector, symbol))
            if sector_2 == no or sector_2 == No or sector_2 == NO:
                print("no")
            else:
                print("That was not one of the options, please re-enter your selection")
        else:
            print("That was not one of the options, please re-enter your selection")
        
    if goal == "ranking results":
        stock = input("What catagory would you like to see the best stocks in, (Long term stock, short term stock, or highest dividend): ")
        if stock == "Long term stock":
            symbol = input("Input the ticker symbol you would like to see information on: ")
            print(long_term_stock(table))
            
        if stock == "short term stock":
            symbol = input("Input the ticker symbol you would like to see information on: ")
            print(short_term_stock(table))
            
        if stock == "highest dividend":
            symbol = input("Input the ticker symbol you would like to see information on: ")
            print(highest_dividend(table))
            
        else:
            print ("That was not one of the options, please re-enter your selection")
    
    else:
        print("That was not one of the options, please re-enter your selection")
main()