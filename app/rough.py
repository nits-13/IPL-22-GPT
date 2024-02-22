if flag:
                        table = PrettyTable()
                        table.field_names = ["Player Name", "Role", "Country", "Matches Played", "Total Runs", "Total Wickets"]
                        players = teams_json["Players"] 
                        for key, val in players.items():
                            table.add_row([key, val[0], val[1], val[2], val[3], val[4]])
                        answers.append(table)

@app.route('/mainpage', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        query = request.form['query']  # Get the user's query from the form
        response_type, response_data = parsing(query)
        if not response_data:
            ans = "Sorry! We don't have an answer to your question"
            return render_template('mainpage.html', query=query, answer=ans)
        else:
            if response_type == "table":
                table_html = response_data.get_html_string()  # Convert the table to an HTML string
                return render_template('mainpage.html', answer=table_html)
            else:
                ans_str = " ".join(response_data)
                return render_template('mainpage.html', query=query, answer=ans_str)
    return render_template('mainpage.html')