from django.shortcuts import render
from neuralNet.nnHandler import *

# Create your views here.
def index(request):
     return render(request, 'neuralNet/neuralNetHome.html')

def neuralNetImagePredict(request):
     prediction = test()
     return render(request, 'neuralNet/neuralNetSnippet.html', {"num1":"cat", "num2":"num2", "z": prediction})

def neuralNetAddition(request, num1, num2):

     n1=int(num1)
     n2=int(num2)
     x = tf.placeholder(tf.int32)
     y = tf.placeholder(tf.int32)

     add=tf.multiply(x,y)
     with tf.Session() as sess:
          z=sess.run(add,feed_dict={x:n1, y:n2})

     return render(request, 'neuralNet/neuralNetSnippet.html', {"num1":num1, "num2":num2, "z": z})


def simpleAddition(request, num1, num2):
     n1=int(num1)
     n2=int(num2)
     z = n1 + n2

     return render(request, 'neuralNet/neuralNetSnippet.html', {"num1":num1, "num2":num2, "z": z})
