import numpy as np
import random
import string
from model import launchModel
from events import Event
import matplotlib.pyplot as plt
def compareQueues(queue1, queue2, genEvents):
	mx_x_1 = []
	avr_x_1 = []
	mx_y_1 = []
	avr_y_1 = []
	mx_x_2 = []
	avr_x_2 = []
	mx_y_2 = []
	avr_y_2 = []
	for ev_in_sec in range(10, 32, 2):
		mx_1 = []
		avr_1 = []
		mx_2 = []
		avr_2 = []
		for i in range(10):
			events = genEvents(1 / ev_in_sec)
			q = launchModel(events = events, queue = queue1)
			mx_1.append(q.getMax())
			avr_1.append(q.getAverage())
			q = launchModel(events = events, queue = queue2)
			mx_2.append(q.getMax())
			# print(q.getMax())
			avr_2.append(q.getAverage())
		mx_y_1.append(np.mean(mx_1))
		avr_y_1.append(np.mean(avr_1))
		mx_x_1.append(ev_in_sec)
		avr_x_1.append(ev_in_sec)
		mx_y_2.append(np.mean(mx_2))
		avr_y_2.append(np.mean(avr_2))
		mx_x_2.append(ev_in_sec)
		avr_x_2.append(ev_in_sec)
	plt.plot(avr_x_1, avr_y_1, 'r', label=type(queue1).__name__)
	plt.xlabel("Средний интервал между посылками, с")
	plt.plot(avr_x_2, avr_y_2, 'b', label=type(queue2).__name__)
	plt.ylabel("Среднее время ожидания, с")
	plt.legend()
	plt.show()
	plt.plot(mx_x_1, mx_y_1, 'r', label=type(queue1).__name__)
	plt.xlabel("Средний интервал между посылками, с")
	plt.plot(mx_x_2, mx_y_2, 'b', label=type(queue2).__name__)
	plt.ylabel("Максимальное время ожидания, с")
	plt.legend()
	plt.show()
