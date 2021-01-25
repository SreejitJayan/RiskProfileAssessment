#
# hello-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json
import pickle
import os

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    name = [3,2,0,0,1,1,2,2,1,2,5,2,0,0,1,3,2,5,4,4,3,2]
    try:
        body = json.loads(data.getvalue())
        age = body.get("age")
        education = body.get("education")
        jobType = body.get("jobType")
        pension = body.get("pension")
        primarySourceOfIncome = body.get("primarySourceOfIncome")
        retired = body.get("retired")
        secondarySourceOfIncome = body.get("secondarySourceOfIncome")
        investmentHorizon = body.get("investmentHorizon")
        understandingOfMarket = body.get("understandingOfMarket")
        married = body.get("married")
        spouseWorking = body.get("spouseWorking")
        familyAnnualIncome = body.get("familyAnnualIncome")
        noOfDependent = body.get("noOfDependent")
        rent = body.get("rent")
        rentCost = body.get("rentCost")
        liabilities = body.get("liabilities")
        investmentObjective = body.get("investmentObjective")
        investmentApproach = body.get("investmentApproach")
        nonPerformingPortfolio = body.get("nonPerformingPortfolio")
        insured = body.get("insured")
        annualIncome = body.get("annualIncome")
        balanceFromInvestment = body.get("balanceFromInvestment")
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)
    
    
    if age == '<25':
      ageML = 4
    elif age == '>=25<40':
      ageML = 3
    elif age == '>=40<58':
      ageML = 2
    elif age == '>=58':
      ageML = 1
    else:
      ageML = 0

    if education == 'Graduate':
      educationML = 2
    elif education == 'Under-Graduate':
      educationML = 1
    elif education == 'Post-Graduate':
      educationML = 3
    else:
      educationML = 0

    if jobType == 'Permanent':
      jobTypeML = 2
    elif jobType == 'Temporary':
      jobTypeML = 1
    else:
      jobTypeML = 0

    if pension == 'Yes':
      pensionML = 2
    elif pension == 'No':
      pensionML = 1
    else:
      pensionML = 0

    if primarySourceOfIncome == 'Salaried':
      primarySourceOfIncomenML = 3
    elif primarySourceOfIncome == 'Pension':
      primarySourceOfIncomenML = 1
    elif primarySourceOfIncome == 'Business':
      primarySourceOfIncomenML = 2
    else:
      primarySourceOfIncomenML = 0

    if retired == 'Yes':
      retiredML = 1
    elif retired == 'No':
      retiredML = 2
    else:
      retiredML = 0

    if secondarySourceOfIncome == 'Rental':
      secondarySourceOfIncomeML = 3
    elif secondarySourceOfIncome == 'Private Channel':
      secondarySourceOfIncomeML = 2
    elif secondarySourceOfIncome == 'Freelancer':
      secondarySourceOfIncomeML = 1
    elif secondarySourceOfIncome == 'Trainer':
      secondarySourceOfIncomeML = 5
    elif secondarySourceOfIncome == 'Stock Broker':
      secondarySourceOfIncomeML = 7
    elif secondarySourceOfIncome == 'Home Based Business':
      secondarySourceOfIncomeML = 6
    else:
      secondarySourceOfIncomeML = 0

    if investmentHorizon == 'Less than a year':
      investmentHorizonML = 1
    elif investmentHorizon == 'upto 2 year':
      investmentHorizonML = 2
    elif investmentHorizon == '2-5 year':
      investmentHorizonML = 3
    elif investmentHorizon == '5-10 years':
      investmentHorizonML = 4
    elif investmentHorizon == 'more than 10 years':
      investmentHorizonML = 5
    else:
      investmentHorizonML = 0

    if understandingOfMarket == 'No Idea':
      understandingOfMarketML = 1
    elif understandingOfMarket == 'Basic':
      understandingOfMarketML = 2
    elif understandingOfMarket == 'Moderate':
      understandingOfMarketML = 3
    elif understandingOfMarket == 'Experianced':
      understandingOfMarketML = 4
    else:
      understandingOfMarketML = 0

    if married == 'Yes':
      marriedML = 1
    elif married == 'No':
      marriedML = 2
    else:
      marriedML = 0

    if spouseWorking == 'Yes':
      spouseWorkingML = 2
    elif spouseWorking == 'No':
      spouseWorkingML = 1
    else:
      spouseWorkingML = 0

    if familyAnnualIncome == 'Less than $30000':
      familyAnnualIncomeML = 1
    elif familyAnnualIncome == '$30000 to $80000':
      familyAnnualIncomeML = 2
    elif familyAnnualIncome == '$80000 to $150000':
      familyAnnualIncomeML = 3
    elif familyAnnualIncome == '$150000 to $250000':
      familyAnnualIncomeML = 4
    elif familyAnnualIncome == '>$250000':
      familyAnnualIncomeML = 5
    else:
      familyAnnualIncomeML = 0

    if noOfDependent == '0':
      noOfDependentML = 5
    elif noOfDependent == '1':
      noOfDependentML = 4
    elif noOfDependent == '2':
      noOfDependentML = 3
    elif noOfDependent == '<3':
      noOfDependentML = 2
    else:
      noOfDependentML = 0

    if rent == 'Own':
      rentML = 2
    elif rent == 'Rental':
      rentML = 1
    else:
      rentML = 0

    if rentCost == '<$1000':
      rentCostML = 4
    elif rentCost == '>$1000<$2000':
      rentCostML = 3
    elif rentCost == '>$2000<$3500':
      rentCostML = 2
    elif rentCost == '>$3500':
      rentCostML = 1
    else:
      rentCostML = 0

    if liabilities == 'Auto':
      liabilitiesML = 4
    elif liabilities == 'Education Loan':
      liabilitiesML = 3
    elif liabilities == 'Home Loan':
      liabilitiesML = 2
    elif liabilities == 'Personal Loan':
      liabilitiesML = 1
    else:
      liabilitiesML = 0

    if investmentObjective == 'Children Education':
      investmentObjectiveML = 5
    elif investmentObjective == 'Savings':
      investmentObjectiveML = 3
    elif investmentObjective == 'Retirement Planning':
      investmentObjectiveML = 5
    elif investmentObjective == 'Kid Wedding':
      investmentObjectiveML = 5
    elif investmentObjective == 'Holidays':
      investmentObjectiveML = 2
    else:
      investmentObjectiveML = 0

    if nonPerformingPortfolio == 'upto 3 months':
      nonPerformingPortfolioML = 1
    elif nonPerformingPortfolio == 'upto 6 month':
      nonPerformingPortfolioML = 2
    elif nonPerformingPortfolio == 'upto 1 year':
      nonPerformingPortfolioML = 3
    elif nonPerformingPortfolio == 'more than a year':
      nonPerformingPortfolioML = 4
    else:
      nonPerformingPortfolioML = 0

    if insured == 'Yes':
      insuredML = 2
    elif insured == 'No':
      insuredML = 1
    else:
      insuredML = 0

    if annualIncome == 'Less than $30000':
      annualIncomeML = 1
    elif annualIncome == '$30000 to $80000':
      annualIncomeML = 2
    elif annualIncome == '$80000 to $150000':
      annualIncomeML = 3
    elif annualIncome == '$150000 to $250000':
      annualIncomeML = 4
    elif annualIncome == '>$250000':
      annualIncomeML = 5
    else:
      annualIncomeML = 0

    if balanceFromInvestment == 'Preferably guaranteed returns before tax savings':
      balanceFromInvestmentML = 1
    elif balanceFromInvestment == 'Stable reliable returns minimal tax savings':
      balanceFromInvestmentML = 2
    elif balanceFromInvestment == 'Some variability in returns some tax savings':
      balanceFromInvestmentML = 3
    elif balanceFromInvestment == 'Moderate variability in returns reasonable tax savings':
      balanceFromInvestmentML = 4
    elif balanceFromInvestment == 'Unstable but potentially higher returns maximize tax savings':
      balanceFromInvestmentML = 5
    else:
      balanceFromInvestmentML = 0


    testing = [[ageML,educationML,primarySourceOfIncomeML,jobTypeML,retiredML,pensionML,
           secondarySourceOfIncomeML,investmentHorizonML,understandingOfMarketML,
           marriedML,noOfDependentML,annualIncomeML,spouseWorkingML,familyAnnualIncomeML,
           rentML,rentCostML,liabilitiesML,investmentObjectiveML,balanceFromInvestmentML,investmentApproachML,
           nonPerformingPortfolioML,insuredML]]

    print("Vale of value = ", name, flush=True)
    print("Exiting Python Hello World handler", flush=True)
    filename = 'finalized_model.sav'
    
    model_dir = os.path.dirname(os.path.realpath(__file__))
    contents = os.listdir(model_dir)
    if filename in contents:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "rb") as file:
            loaded_model = pickle.load(file)
        result = loaded_model.predict(testing)
    else:
        raise Exception('{0} is not found in model directory {1}'.format(filename, model_dir))

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Your risk appetite is {0} percent".format(result)}),
        headers={"Content-Type": "application/json"}
    )
