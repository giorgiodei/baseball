from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.year from teams t where t.year>=1980"""
        cursor.execute(query)

        for row in cursor:
            result.append(int(row['year']))
        cursor.close()
        conn.close()
        return result


    def getTeamsOfYear(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
from teams t
where t.`year`= %s"""
        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result

    def getSalariesTeam(year, idMapTeams):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.ID , t.teamCode ,sum(s.salary) as totSalary
from salaries s , teams t , appearances a 
where s.year=t.year  and t.`year` =a.`year` and a.`year`=%s
and t.id=a.teamID and a.playerID =s.playerID 
group by t.ID , t.teamCode  """
        cursor.execute(query, (year,))

        MapSalary={}
        for row in cursor:
            MapSalary[idMapTeams[row["ID"]]]=row["totSalary"] # chiave =team, valore= somma dei salari

        cursor.close()
        conn.close()
        return result



