from flask import Flask, request, render_template,Markup,flash
import Training as tr
import random
from textblob import TextBlob, Word
import webbrowser
import wikipedia
from datetime import datetime
import pygame,sys,random
import pandas as pd
import csv
import pygame,sys,random

class Authenticator():
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def register(self):
        file = open("Userdetails.txt", "r+")
        j=False
        for i in file:
            a=i.split(',')
            y=len(a)
            for p in range(0,y-1):
                if(a[p]==self.username):
                    j=True
                else:
                    continue
        if(j==False):
            global k
            if (len(self.password) < 7):
                k = "Password length is too short"
            else:
                e="@"
                u="#"
                m="%"
                z="^"
                v="&"
                if e in self.password:
                    file.write(self.username + "," + self.password + "\n")
                    k = "Registered successfully"
                elif u in self.password:
                    file.write(self.username + "," + self.password + "\n")
                    k = "Registered successfully"
                elif m in self.password:
                    file.write(self.username + "," + self.password + "\n")
                    k = "Registered successfully"
                elif z in self.password:
                    file.write(self.username + "," + self.password + "\n")
                    k = "Registered successfully"
                elif v in self.password:
                    file.write(self.username + "," + self.password + "\n")
                    k = "Registered successfully"
                else:
                    k="Password must contain @ or # or % or ^ or &"
        else:
            k="Username Already exists"
        file.close()

    def login(self):
        file = open("Userdetails.txt", "r")
        L = False
        for i in file:
            a, b = i.split(',')
            b = b.strip()
            c = str(b)
            if (a == self.username and c == self.password):
                L = True
                break
        file.close()
        if (L == True):
            global z
            z = "Logged in Successfully"
        else:
            z = "Username or Password is incorrect"

        file.close()





class bot(Authenticator):
    global q
    def __init__(self, message):
        self.message = message

    def search(self):
        i = self.message
        b=i.lower()
        c = str(b)
        u=False
        h = len(tr.greetings)
        y=False
        for i in range(0,h-1):
            if(c== tr.greetings[i]):
                k = random.randrange(0, 3)
                q=tr.greetings_response[k]
                u=True
                return q
        h=len(tr.task)
        for i in range(0,h-1):
            if(c==tr.task[i]):
                q=tr.task_response
                u=True
                return q
        h=len(tr.name)
        for i in range(0,h-1):
            if(c==tr.name[i]):
                q=tr.name_response
                u=True
                return q
        h=len(tr.age)
        for i in range(0,h-1):
            if(c==tr.age[i]):
                q=tr.age_response
                u = True
                return q
        h=len(tr.goodbye)
        for i in range(0,h-1):
            if(c==tr.goodbye[i]):
                k=random.randrange(0,3)
                q=tr.goodbye_response[k]
                u = True
                return q
        h = len(tr.jokes)
        for i in range(0, h - 1):
            if (c == tr.jokes[i]):
                k = random.randrange(0, 7)
                q = tr.jokes_response[k]
                u = True
                return q
        h=len(tr.story)
        for i in range(0, h - 1):
            if (c == tr.story[i]):
                k = random.randrange(0, 5)
                q = tr.story_response[k]
                u = True
                return q
        h=len(tr.dates)
        for i in range(0,h-1):
            if(c==tr.dates[i]):
                now=datetime.now()
                dt=now.strftime("%d/%m/%Y %H:%M:%S")
                return dt
        a='motivational'
        if a in c:
            df = pd.read_csv('quotes_data.csv', encoding='latin1')
            new = df["hrefs"].str.split("src=t_", n=1, expand=True)
            df['quotes_type'] = new[1]
            author = df["lines"].str.split(".-", n=1, expand=True)
            df["quotes_lines"] = author[0]
            dataset = df.drop(['lines', 'hrefs'], axis=1)
            df_new = dataset.groupby('quotes_type').agg({'quotes_lines': ', '.join}).reset_index()
            final_df = df_new[['quotes_type', 'quotes_lines']]
            question = list(final_df['quotes_type'])
            for index, row in final_df.iterrows():
                ques = row['quotes_type']
                ans = row['quotes_lines']
                sentence = random.choice(df["quotes_lines"])
                q=sentence
                return q
        a='capital of'
        if a in c:
            try:
                results=wikipedia.summary(c,sentences=3)
                return results
            except wikipedia.exceptions.PageError:
                query = c
                search = query.replace(" ", "+")
                url = f"https://www.google.com/search?q={search}"
                webbrowser.get().open(url)
                return "Opening with google"
        a = 'captain of'
        if a in c:
            try:
                results = wikipedia.summary(c,sentences=2)
                return results
            except wikipedia.exceptions.PageError:
                query = c
                search = query.replace(" ", "+")
                url = f"https://www.google.com/search?q={search}"
                webbrowser.get().open(url)
                return "Opening with google"
        a = 'wikipedia'
        if a in c:
            d=c.replace("wikipedia","")
            try:
                results = wikipedia.summary(d)
                return results
            except wikipedia.exceptions.PageError:
                query = c
                search = query.replace(" ", "+")
                url = f"https://www.google.com/search?q={search}"
                webbrowser.get().open(url)
                return "Opening with google"



        if(u==False):
            sentence=TextBlob(c)
            p=sentence.sentiment.polarity
            if(p<0):
                k=random.randrange(0,4)
                q=tr.sad_responses[k]
                return q
            else:
                d=b.split(" ")
                r=len(d)
                o="play"
                a='youtube'
                if o in c:
                    c=c.replace("play","")
                    query = c
                    search = query.replace(" ", "+")
                    url = f"https://www.youtube.com/results?search_query={search}"
                    webbrowser.get().open(url)
                    return "Opening with Youtube"
                elif a in c:
                    c=c.replace("youtube","")
                    query = c
                    search = query.replace(" ", "+")
                    url = f"https://www.youtube.com/results?search_query={search}"
                    webbrowser.get().open(url)
                    return "Opening with Youtube"
                else:
                    query = c
                    search = query.replace(" ", "+")
                    url = f"https://www.google.com/search?q={search}"
                    webbrowser.get().open(url)
                    return "Opening with google"

class Convo(Authenticator):
    def __init__(self,text,number,no):
        self.text=text
        self.number=number
        self.no=no
    def searching(self):
        c=self.text
        h=c.lower()
        if "you" in h:
            if(self.number==0):
                return tr.sports_reponses[self.no]
            if(self.number==1):
                return tr.games_response[self.no]
            if(self.number==2):
                return tr.travel_response[self.no]
            if(self.number==3):
                return tr.food_response[self.no]
            if(self.number==4):
                return tr.music_response[self.no]
            if(self.number==5):
                return tr.movies_response[self.no]
        else:
            g=random.randrange(0,7)
            return tr.response[g]

def topics():
    k = random.randrange(0,6)
    j = tr.randomtopics_response[k]
    if (j == "Sports"):
        h = random.randrange(0, 5)
        y=tr.sports[h]
        return y,k,h

    elif (j == "Games"):
        h = random.randrange(0, 6)
        y = tr.games[h]
        return y,k,h
    elif (j == "Travel"):
        h = random.randrange(0, 4)
        y = tr.travel[h]
        return y,k,h
    elif (j == "Food"):
        h = random.randrange(0, 4)
        y = tr.food[h]
        return y,k,h
    elif(j=="Music"):
        h=random.randrange(0,5)
        y=tr.music[h]
        return y,k,h
    else:
        h=random.randrange(0,5)
        y=tr.movies[h]
        return y,k,h


def game():
    def floor():
        screen.blit(floor_surface, (floor_x_pos, 900))
        screen.blit(floor_surface, (floor_x_pos + 576, 900))

    def pipe():
        pipeposition = random.choice(pipe_height)
        pipe_bottom = pipe_surface.get_rect(midtop=(700, pipeposition))
        pipe_top = pipe_surface.get_rect(midbottom=(700, pipeposition - 300))
        return pipe_bottom, pipe_top

    def pipemovement(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        pipes_shown = [pipe for pipe in pipes if pipe.right > -50]
        return pipes_shown

    def pipelength(pipes):
        for pipe in pipes:
            if pipe.bottom >= 1024:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def collision(pipes):
        global can_score
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                death_sound.play()
                can_score = True
                return False

        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            can_score = True
            return False

        return True

    def birdturn(bird):
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def animation_bird():
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
        return new_bird, new_bird_rect

    def scoredisp(game_state):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(288, 850))
            screen.blit(high_score_surface, high_score_rect)

    def newscore(score, high_score):
        if score > high_score:
            high_score = score
        return high_score

    def check_pipescore():
        global score
        score=0
        global can_score

        if pipe_list:
            for pipe in pipe_list:
                if 95 < pipe.centerx < 105 and can_score:
                    score+= 1
                    score_sound.play()
                    can_score = False
                if pipe.centerx < 0:
                    can_score = True

    pygame.init()
    screen = pygame.display.set_mode((576, 1024))
    clock = pygame.time.Clock()
    game_font = pygame.font.Font('04B_19.ttf', 40)

    gravity = 0.25
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    can_score = True
    bg_surface = pygame.image.load('assets/background-day.png').convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

    floor_surface = pygame.image.load('assets/base.png').convert()
    floor_surface = pygame.transform.scale2x(floor_surface)
    floor_x_pos = 0

    bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
    bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
    bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
    bird_frames = [bird_downflap, bird_midflap, bird_upflap]
    bird_index = 0
    bird_surface = bird_frames[bird_index]
    bird_rect = bird_surface.get_rect(center=(100, 512))

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    pipe_surface = pygame.image.load('assets/pipe-green.png')
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    pipe_height = [400, 600, 800]

    game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
    game_over_rect = game_over_surface.get_rect(center=(288, 512))

    flap_sound = pygame.mixer.Sound('sounds/sound_sfx_wing.wav')
    death_sound = pygame.mixer.Sound('sounds/sound_sfx_hit.wav')
    score_sound = pygame.mixer.Sound('sounds/sound_sfx_point.wav')
    score_sound_countdown = 100
    SCOREEVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(SCOREEVENT, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 12
                    flap_sound.play()
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100, 512)
                    bird_movement = 0
                    score = 0

            if event.type == SPAWNPIPE:
                pipe_list.extend(pipe())

            if event.type == BIRDFLAP:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0

                bird_surface, bird_rect = animation_bird()

        screen.blit(bg_surface, (0, 0))

        if game_active:
            bird_movement += gravity
            rotated_bird = birdturn(bird_surface)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird, bird_rect)
            game_active = collision(pipe_list)

            pipe_list = pipemovement(pipe_list)
            pipelength(pipe_list)

            check_pipescore()
            scoredisp('main_game')
        else:
            screen.blit(game_over_surface, game_over_rect)
            high_score = newscore(score, high_score)
            scoredisp('game_over')

        floor_x_pos -= 1
        floor()
        if floor_x_pos <= -576:
            floor_x_pos = 0

        pygame.display.update()
        clock.tick(120)





stepgoals = 10000  # default value for number of steps to get done in a day
timegoals = 60  # defualt value for number of minutes one should spend exercising in one day

class Fitness():
    def __init__(self,diastolicpressure,systolicpressure,steps,exercise):
        self.diastolicpressure=diastolicpressure
        self.systolicpressure=systolicpressure
        self.steps=steps
        self.exercise=exercise

    def details(self):
        b=int(self.diastolicpressure)
        c=int(self.systolicpressure)
        if b > 100 or c > 140:
            z=len(tr.highbp)
            y=random.randrange(0,z-1)
            global q
            q=tr.highbp[y]
            return q
        elif b > 90 or c > 130:
            z=len(tr.mediumbp)
            y=random.randrange(0,z-1)
            q=tr.mediumbp[y]
            return q
        elif b > 70 or c > 110:
            q="That's great! Loving the perfect results!"
            return q
        elif b > 50 or c > 90:
            z=len(tr.lowbp)
            y=random.randrange(0,z-1)
            q=tr.lowbp[y]
            return q
        else:
            z=len(tr.verylowbp)
            y=random.randrange(0,z-1)
            q=tr.verylowbp[y]
            return q

    def exec_bot(self):
        global qt
        h=int(self.steps)
        if h >= stepgoals:
            z = len(tr.dailygoals)
            y = random.randrange(0, z - 1)
            qt = tr.dailygoals[y]
            return qt
        else:
            z = len(tr.closegoals)
            y = random.randrange(0, z - 1)
            qt = tr.closegoals[y]
            return qt

    def repeatexec(self):
        global qq
        r=int(self.exercise)
        if r >= timegoals:
            z = len(tr.dailygoals)
            y = random.randrange(0, z - 1)
            qq = tr.dailygoals[y]
            return qq
        else:
            z = len(tr.closegoals)
            y = random.randrange(0, z - 1)
            qq = tr.closegoals[y]
            return qq

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def submit():
    return render_template('Index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        name = request.form['Username']
        pwd = request.form['Password']
        pd=request.form['Password2']
        if(pd==pwd):
            n = str(name)
            h = str(pwd)
            obj = Authenticator(n,h)
            obj.register()
            return k
        else:
            return "Both passwords are not same"
    else:
        return render_template("Register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        name = request.form['Username']
        pwd = request.form['Password']
        global n
        n = str(name)
        h = str(pwd)
        obj = Authenticator(n,h)
        obj.login()
        if(z=="Logged in Successfully"):
            return render_template("Button.html")
        else:
            return "Username or Password is incorrect"
    else:
        return render_template("Login.html")


@app.route('/login/chatbot',methods=['GET','POST'])
def chatbot():
    if(request.method=='POST'):
        text=request.form['Text']
        usertext = bot(text)
        flash(usertext.search())
        return render_template("Chatbot.html")

    else:
        return render_template("Chatbot.html")

@app.route('/login/chatbot/convo',methods=['GET','POST'])
def convo():
    a, b, c = topics()
    flash(a, 'questions')
    if(request.method=='POST'):
        text=request.form['Text']
        data=str(text)
        userconvo = Convo(data,b,c)
        flash(userconvo.searching(),'userresponse')
        return render_template("convo.html")
    else:
        return render_template("convo.html")



@app.route('/login/Flappybird',methods=['GET','POST'])
def flappybird():
    return game()




@app.route('/login/fitness',methods=['GET','POST'])
def fitbot():
    z=len(tr.fitness)
    y=random.randrange(0,z-1)
    g=tr.fitness[y]
    flash(g,'niceday')
    w=len(tr.diastolic)
    o=random.randrange(0,w-1)
    u=tr.diastolic[o]
    flash(u,'diastolic')
    op = len(tr.systolic)
    qw = random.randrange(0, op - 1)
    us = tr.systolic[qw]
    flash(us, 'systolic')
    st = len(tr.steps)
    qwe = random.randrange(0, st - 1)
    ut = tr.steps[qwe]
    flash(ut, 'steps')
    stee = len(tr.exercise)
    qwet = random.randrange(0, stee - 1)
    uts = tr.exercise[qwet]
    flash(uts, 'exercise')

    if(request.method=='POST'):
        diastolic=request.form['Diastolic']
        systolic=request.form['systolic']
        steps=request.form['steps']
        exercise=request.form['exercise']
        obj=Fitness(diastolic,systolic,steps,exercise)
        obj.details()
        flash(q,"pressure")
        obj.exec_bot()
        spy=str(qt)
        pye="For steps:"+spy
        flash(pye,"stepss")
        obj.repeatexec()
        spot=str(qq)
        spots="For time:"+spot
        flash(spots,"timegoals")
        fields=[str(n),str(diastolic),str(systolic),str(steps),str(exercise)]
        filename="Records.csv"
        with open(filename,'w') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerows(fields)

    return render_template("Fitness.html")



if __name__ == "__main__":
    app.secret_key='secret_key'
    app.config['SESSION_TYPE']='filesystem'
    app.run(debug=True)
