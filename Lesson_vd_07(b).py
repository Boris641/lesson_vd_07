from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Фиктивные данные пользователя для примера
user_profile = {
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "password": "password123"  # В реальном приложении пароли должны храниться в зашифрованном виде
}

@app.route('/')
def index():
    return redirect(url_for('edit_profile'))

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        user_profile['name'] = request.form['name']
        user_profile['email'] = request.form['email']
        user_profile['password'] = request.form['password']
        return redirect(url_for('profile_updated'))
    return render_template('edit_profile.html', profile=user_profile)

@app.route('/profile-updated')
def profile_updated():
    return "Профиль успешно обновлен! <a href='/edit-profile'>Вернуться к редактированию</a>"

if __name__ == '__main__':
    app.run(debug=True)