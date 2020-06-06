from flask import Flask, render_template
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf import form
from werkzeug.utils import redirect

from Project_3.data import db_session
from Project_3.data.register import RegisterForm, LoginForm
from Project_3.data.users import User
from flask_bootstrap import Bootstrap

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
bootstrap = Bootstrap(app)


class Bookmarks(object):
    pass


def main():
    db_session.global_init("db/db.sqlite")

    @app.route("/")
    def index():
        return render_template("index.html")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    @app.route('/login/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            session = db_session.create_session()
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")

            user = User(
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data
            )

            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация.', form=form)

    @app.route('/login/', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            user = session.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("change")
            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)
        return render_template('login.html', title='Авторизация.', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect("/")

    @app.route('/leaders')
    def leaders_list():
        return render_template('leaders_list.html', title='Наша гордость.', form=form)

    @app.route('/login/change')
    @login_required
    def change():
        return render_template('change_menu.html', title='Уроки.', form=form)

    @app.route('/login/tests')
    @login_required
    def tests_list():
        return render_template('tests_list.html', title='Тесты.', form=form)

    @app.route('/login/literature')
    @login_required
    def literature():
        return render_template('literature.html', title='Теоретическая часть.', form=form)

    @app.route('/login/lit')
    @login_required
    def lit():
        return render_template('lit.html', title='Теоретическая часть.', form=form)

    # Русский язык
    @app.route('/login/rus/1')
    def rus_test_1():
        return render_template('tests_rus1.html', title='Русский язык. Задание 1.', form=form)

    @app.route('/login/rus/2')
    def rus_test_2():
        return render_template('tests_rus2.html', title='Русский язык. Задание 2.', form=form)

    @app.route('/login/rus/3')
    def rus_test_3():
        return render_template('tests_rus3.html', title='Русский язык. Задание 3.', form=form)

    @app.route('/login/rus/4')
    def rus_test_4():
        return render_template('tests_rus4.html', title='Русский язык. Задание 4.', form=form)

    @app.route('/login/rus/5')
    def rus_test_5():
        return render_template('tests_rus5.html', title='Русский язык. Задание 5.', form=form)

    @app.route('/login/rus/6')
    def rus_test_6():
        return render_template('tests_rus6.html', title='Русский язык. Задание 6.', form=form)

    @app.route('/login/rus/result')
    def rus_test_result():
        return render_template('tests_rus_result.html', title='Русский язык. Результат.', form=form)

    # Литература
    @app.route('/login/lit/1')
    def lit_test_1():
        return render_template('tests_lit1.html', title='Литература. Задание 1.', form=form)

    @app.route('/login/lit/2')
    def lit_test_2():
        return render_template('tests_lit2.html', title='Литература. Задание 2.', form=form)

    @app.route('/login/lit/3')
    def lit_test_3():
        return render_template('tests_lit3.html', title='Литература. Задание 3.', form=form)

    @app.route('/login/lit/4')
    def lit_test_4():
        return render_template('tests_lit4.html', title='Литература. Задание 4.', form=form)

    @app.route('/login/lit/5')
    def lit_test_5():
        return render_template('tests_lit5.html', title='Литература. Задание 5.', form=form)

    @app.route('/login/lit/6')
    def lit_test_6():
        return render_template('tests_lit6.html', title='Литература. Задание 6.', form=form)

    @app.route('/login/lit/result')
    def lit_test_result():
        return render_template('tests_lit_result.html', title='Литература. Результат.', form=form)

    # Английский
    @app.route('/login/eng/1')
    def eng_test_1():
        return render_template('tests_eng1.html', title='Английский. Задание 1.', form=form)

    @app.route('/login/eng/2')
    def eng_test_2():
        return render_template('tests_eng2.html', title='Английский. Задание 2.', form=form)

    @app.route('/login/eng/3')
    def eng_test_3():
        return render_template('tests_eng3.html', title='Английский. Задание 3.', form=form)

    @app.route('/login/eng/4')
    def eng_test_4():
        return render_template('tests_eng4.html', title='Английский. Задание 4.', form=form)

    @app.route('/login/eng/5')
    def eng_test_5():
        return render_template('tests_eng5.html', title='Английский. Задание 5.', form=form)

    @app.route('/login/eng/6')
    def eng_test_6():
        return render_template('tests_eng6.html', title='Английский. Задание 6.', form=form)

    @app.route('/login/eng/result')
    def eng_test_result():
        return render_template('tests_eng_result.html', title='Английский. Результат.', form=form)

    # Французский
    @app.route('/login/fr/1')
    def fr_test_1():
        return render_template('tests_fr1.html', title='Французский. Задание 1.', form=form)

    @app.route('/login/fr/2')
    def fr_test_2():
        return render_template('tests_fr2.html', title='Французский. Задание 2.', form=form)

    @app.route('/login/fr/3')
    def fr_test_3():
        return render_template('tests_fr3.html', title='Французский. Задание 3.', form=form)

    @app.route('/login/fr/4')
    def fr_test_4():
        return render_template('tests_fr4.html', title='Французский. Задание 4.', form=form)

    @app.route('/login/fr/5')
    def fr_test_5():
        return render_template('tests_fr5.html', title='Французский. Задание 5.', form=form)

    @app.route('/login/fr/6')
    def fr_test_6():
        return render_template('tests_fr6.html', title='Французский. Задание 6.', form=form)

    @app.route('/login/fr/result')
    def fr_test_result():
        return render_template('tests_fr_result.html', title='Французский. Результат.', form=form)

    # Математика
    @app.route('/login/math/1')
    def math_test_1():
        return render_template('tests_math1.html', title='Математика. Задание 1.', form=form)

    @app.route('/login/math/2')
    def math_test_2():
        return render_template('tests_math2.html', title='Математика. Задание 2.', form=form)

    @app.route('/login/math/3')
    def math_test_3():
        return render_template('tests_math3.html', title='Математика. Задание 3.', form=form)

    @app.route('/login/math/4')
    def math_test_4():
        return render_template('tests_math4.html', title='Математика. Задание 4.', form=form)

    @app.route('/login/math/5')
    def math_test_5():
        return render_template('tests_math5.html', title='Математика. Задание 5.', form=form)

    @app.route('/login/math/6')
    def math_test_6():
        return render_template('tests_math6.html', title='Математика. Задание 6.', form=form)

    @app.route('/login/math/result')
    def math_test_result():
        return render_template('tests_math_result.html', title='Математика. Результат.', form=form)

    # Алгебра
    @app.route('/login/alg/1')
    def alg_test_1():
        return render_template('tests_alg1.html', title='Алгебра. Задание 1.', form=form)

    @app.route('/login/alg/2')
    def alg_test_2():
        return render_template('tests_alg2.html', title='Алгебра. Задание 2.', form=form)

    @app.route('/login/alg/3')
    def alg_test_3():
        return render_template('tests_alg3.html', title='Алгебра. Задание 3.', form=form)

    @app.route('/login/alg/4')
    def alg_test_4():
        return render_template('tests_alg4.html', title='Алгебра. Задание 4.', form=form)

    @app.route('/login/alg/5')
    def alg_test_5():
        return render_template('tests_alg5.html', title='Алгебра. Задание 5.', form=form)

    @app.route('/login/alg/6')
    def alg_test_6():
        return render_template('tests_alg6.html', title='Алгебра. Задание 6.', form=form)

    @app.route('/login/alg/result')
    def alg_test_result():
        return render_template('tests_alg_result.html', title='Алгебра. Результат.', form=form)

    # Геометрия
    @app.route('/login/geom/1')
    def geom_test_1():
        return render_template('tests_geom1.html', title='Геометрия. Задание 1.', form=form)

    @app.route('/login/geom/2')
    def geom_test_2():
        return render_template('tests_geom2.html', title='Геометрия. Задание 2.', form=form)

    @app.route('/login/geom/3')
    def geom_test_3():
        return render_template('tests_geom3.html', title='Геометрия. Задание 3.', form=form)

    @app.route('/login/geom/4')
    def geom_test_4():
        return render_template('tests_geom4.html', title='Геометрия. Задание 4.', form=form)

    @app.route('/login/geom/5')
    def geom_test_5():
        return render_template('tests_geom5.html', title='Геометрия. Задание 5.', form=form)

    @app.route('/login/geom/6')
    def geom_test_6():
        return render_template('tests_geom6.html', title='Геометрия. Задание 6.', form=form)

    @app.route('/login/geom/result')
    def geom_test_result():
        return render_template('tests_geom_result.html', title='Геометрия. Результат.', form=form)

    app.run()


if __name__ == '__main__':
    main()
