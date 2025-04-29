from datetime import datetime
import re
def get_days_from_today(date):
    without_separators_pattern = r"([;,\-:\.])"
    without_separators_replacement = ""
    without_separators_date = re.sub(without_separators_pattern,without_separators_replacement,date)
    pattern = r"(\d{4})(\d{2})(\d{2})"
    replacement = r"\1-\3-\6"
    formatted_date = re.sub(pattern,replacement,without_separators_date)
    now_date = datetime.now().date()
    current_date = datetime.strptime(formatted_date,"%Y-%m-%d").date()
    diff = now_date - current_date
    return diff.days
    
print(get_days_from_today("2026:10:09"))