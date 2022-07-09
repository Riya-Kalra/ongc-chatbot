# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3

class ActionDetailSearch(Action):
#
    def name(self) -> Text:
       return "action_detail_search"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         eeid = tracker.get_slot("e_id")
         employee= sqlite3.connect("Employee.db")

         sql1= "select ename from Employee where eid = '"+str(eeid)+"';"
         sql2= "select edesignation from Employee where eid = '"+str(eeid)+"';"
         sql3= "select esalary from Employee where eid = '"+str(eeid)+"';"
         sql4="select ephoneno from Employee where eid = '"+str(eeid)+"';"
         sql5="select ejoindate from Employee where eid = '"+str(eeid)+"';"
         sql6="select eleaves from Employee where eid = '"+str(eeid)+"';"
         curemp = employee.cursor()
         curemp.execute(sql1)
         name=curemp.fetchone()
         if name == None:
              dispatcher.utter_message("Sorry, we are at the learing stating we don't have that detail or may be you have provided us the wrong id.")
         else:
              name= ''.join(name)
              curemp.execute(sql2)
              designation=curemp.fetchone()
              designation= ''.join(designation)
              curemp.execute(sql3)
              salary = curemp.fetchone()
              salary = float(salary[0])
              curemp.execute(sql4)
              phoneno = curemp.fetchone()
              phoneno = int(phoneno[0])
              curemp.execute(sql5)
              joiningdate = curemp.fetchone()
              joiningdate = str(joiningdate[0])
              curemp.execute(sql6)
              leaves = curemp.fetchone()
              leaves = int(leaves[0])
              dispatcher.utter_message("The details of the employee are as follows: \n Employee id is {} \n Employee name is {} \n Employee Designation is {} \n Employee Salary is {} \n Employee Phone no is {} \n Employee joining date is {} \n Number of leaves taken are {} days".format(eeid,name,designation,salary,phoneno,joiningdate,leaves))
#
         return []

class ActionSearchUrl(Action):
#
    def name(self) -> Text:
       return "action_search_url"
#
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         url = tracker.get_slot("url")
         url = url.upper()
         ongcsite = sqlite3.connect("ongcsites.db")

         sql1="select url from websites where name = '"+url+"';"
         ongccur=ongcsite.cursor()
         ongccur.execute(sql1)
         urlname=ongccur.fetchone()
         if urlname==None:
              dispatcher.utter_message("Sorry for the inconvenience, we don't have that link or may be you have provided the wrong name of the site.")
         else:
              urlname=''.join(urlname)
              dispatcher.utter_message("The url of {} is : {}".format(url,urlname))

         return []


