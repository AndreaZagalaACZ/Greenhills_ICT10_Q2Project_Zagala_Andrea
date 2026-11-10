# Adding a new club member
from pyscript import display, document  

def new_member(e):
    document.getElementById('output2').innerHTML = " "
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value

    # Calls out the variables between different batches
    grade7 = {'John Dela Cruz', 'Cassiel Agoncillo', 'Lovity Veritas'}
    grade8 = {'Pytha Theo', 'Livie Cervee'}
    grade9 = {'Squiddo Swag'}
    grade10 = {'Mari Kamimori', 'Zai Jiyan', 'Flee Eljae'}

    # Adding and listing the current members via union
    new_members = {first + last}
    current_members = grade7 | grade8 | grade9 | grade10 |new_members
    # Finding the total member count
    total_members = len(current_members)

    # Output/Result
    document.getElementById('output2').innerHTML = f'Here are the list of members:{current_members}! The total members currently are: {total_members}'
