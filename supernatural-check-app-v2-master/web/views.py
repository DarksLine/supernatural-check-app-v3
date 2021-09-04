from django.shortcuts import render, redirect
from random import randint
from django.views.generic import View


class MainPage(View):

    @classmethod
    def index_view(cls, request):
        request.session["success"] = {'num1': 0, 'num2': 0, 'num3': 0}
        request.session["iter"] = 1
        request.session["proc_succ"] = {'num1': 0, 'num2': 0, 'num3': 0}
        request.session["guess"] = []
        return render(request, 'index.html')

    @classmethod
    def initial_view(cls, request):
        res = {'num1': None, 'num2': None, 'num3': None}
        for element in res:
            res[element] = randint(10, 99)
        request.session["res"] = res
        return render(request, 'initial.html')

    @classmethod
    def percent(cls, request, predict, mind):
        success = request.session["success"]
        for element in predict:
            if predict.get(element) == mind:
                success[element] = success[element] + 1

        percent = {'num1': 0, 'num2': 0, 'num3': 0}
        for element in percent:
            percent[element] = int((success.get(element) / request.session["iter"]) * 100)
        request.session["percent_success"] = success
        return percent

    @classmethod
    def testing_view_get(cls, request):
        return render(request, 'testing.html', request.session["res"])

    @classmethod
    def testing_view_post(cls, request):
        request.session["number_in_head"] = int(request.POST['answer'])
        request.session["proc_succ"] = MainPage.percent(
            request, request.session["res"], request.session["number_in_head"]
            )
        request.session["iter"] += 1
        return redirect('/result')

    @classmethod
    def result_view(cls, request):
        predict = request.session["res"]
        predict['answer'] = request.session["number_in_head"]

        guess = request.session["guess"]
        guess.insert(0, predict)

        request.session["guess"] = guess
        proc_succ = request.session["proc_succ"]
        return render(request, 'result.html', {'dict_res': guess, 'procent_success': proc_succ})