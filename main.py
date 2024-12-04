from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pyodbc

app = FastAPI()

# Paramètres de connexion à la base de données Azure SQL
server = 'server-bd-jep.database.windows.net'  
database = 'bd-jep'  
username = 'adminuser'  
password = 'Admin2024'  
driver = '{ODBC Driver 17 for SQL Server}'  

# Connexion à la base de données Azure SQL
def get_db_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
        )
        return conn
    except Exception as e:
        raise Exception(f"Erreur de connexion à la base de données : {str(e)}")

# Route principale pour afficher la page HTML avec les employés
@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        # Connexion à la base de données
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Récupération des employés
        cursor.execute("SELECT * FROM Employes")
        rows = cursor.fetchall()
        conn.close()

        employes = [
            {"Id": row[0], "Nom": row[1], "Prenom": row[2], "Poste": row[3], "Salaire": row[4]}
            for row in rows
        ]

        # Lecture du fichier HTML
        with open("index.html", "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        # Remplir le template HTML avec les données
        rows_html = ""
        for employe in employes:
            rows_html += f"""
            <tr>
                <td>{employe['Id']}</td>
                <td>{employe['Nom']}</td>
                <td>{employe['Prenom']}</td>
                <td>{employe['Poste']}</td>
                <td>{employe['Salaire']}</td>
            </tr>
            """
        html_content = html_content.replace("{table_rows}", rows_html)

        return HTMLResponse(content=html_content)

    except Exception as e:
        return HTMLResponse(content=f"<h1>Erreur interne</h1><p>{str(e)}</p>", status_code=500)

# Route pour le fichier CSS
@app.get("/style.css", response_class=FileResponse)
def get_styles():
    return "style.css"
