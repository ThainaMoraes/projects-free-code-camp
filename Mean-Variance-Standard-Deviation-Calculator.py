{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5a25b830",
   "metadata": {},
   "source": [
    "## Mean-Variance-Standard Deviation Calculator"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17190b2c",
   "metadata": {},
   "source": [
    "Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.\n",
    "\n",
    "The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.\n",
    "\n",
    "The returned dictionary should follow this format:\n",
    "\n",
    "    {\n",
    "      'mean': [axis1, axis2, flattened],\n",
    "      'variance': [axis1, axis2, flattened],\n",
    "      'standard deviation': [axis1, axis2, flattened],\n",
    "      'max': [axis1, axis2, flattened],\n",
    "      'min': [axis1, axis2, flattened],\n",
    "      'sum': [axis1, axis2, flattened]\n",
    "    }"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcb008c4",
   "metadata": {},
   "source": [
    "If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: \"List must contain nine numbers.\" The values in the returned dictionary should be lists and not Numpy arrays."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9968ba50",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1db3ecf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate(matrix):\n",
    "    dictionary = {}\n",
    "    list_np = [np.mean, np.var, np.std, np.max, np.min, np.sum]\n",
    "    name_np = ['mean','variance','standard devitation','max','min','sum']\n",
    "    dictionary = {}\n",
    "\n",
    "    for i  in range(6):\n",
    "        axis1 = [list_np[i](x) for x in zip(*matrix)]\n",
    "        axis2 = [list_np[i](x) for x in zip(matrix)]\n",
    "\n",
    "        flattened  = list_np[i](axis1 + axis2)\n",
    "        dictionary[name_np[i]] = [axis1, axis2, flattened]\n",
    "    print('\\nmatrix:\\n', matrix)\n",
    "    print('-'*10)\n",
    "    print('calculator:\\n', dictionary)\n",
    "    return matrix, dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9b4dea84",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check(input_answer):\n",
    "    valid = False\n",
    "    while not valid:\n",
    "            try:\n",
    "                input_numbers = input('Type 9 numbers:\\n ')\n",
    "                input_lis = input_numbers.split()\n",
    "                input_listt = [float(i) for i in input_lis]\n",
    "                \n",
    "                if len(input_listt) == 9:\n",
    "                    listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]\n",
    "                    listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]\n",
    "                    matrix = np.array(listt_to_matrix)  \n",
    "                    valid = True\n",
    "                return matrix\n",
    "            except:\n",
    "                print (\"\\nList must contain nine numbers!\\n\")\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c351e155",
   "metadata": {},
   "outputs": [],
   "source": [
    "def initiate(input_answer):   \n",
    "    \n",
    "    if input_answer == 1:     \n",
    "        matrix = check(input_answer)\n",
    "        \n",
    "    elif input_answer == 2:\n",
    "        input_listt = [random.randint(0,100) for i in range(9)]\n",
    "        listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]\n",
    "        matrix = np.array(listt_to_matrix) \n",
    "        \n",
    "    else: first()\n",
    "        \n",
    "    return matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2208a64c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def init():\n",
    "    matrix =  first()\n",
    "    return matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "66427a12",
   "metadata": {},
   "outputs": [],
   "source": [
    "def first():\n",
    "    valid = False\n",
    "    while not valid:\n",
    "            try:\n",
    "                print(\"\\nDo you want to create your matrix or generate a random one?\\n \")\n",
    "                print(\"1 - My own matix\")\n",
    "                print(\"2 - Random matix\")\n",
    "                input_answer = int(input(\"\\n What is your choice? \\n \"))\n",
    "                \n",
    "                if input_answer == 1 or input_answer==2:\n",
    "                    matrix = initiate(input_answer)\n",
    "                    return matrix\n",
    "                    valid = True\n",
    "                \n",
    "            except ValueError:\n",
    "                print (\"You didn't type a number!\\n\")\n",
    "      \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "61f9e86f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to create your matrix or generate a random one?\n",
      " \n",
      "1 - My own matix\n",
      "2 - Random matix\n",
      "\n",
      " What is your choice? \n",
      " l\n",
      "You didn't type a number!\n",
      "\n",
      "\n",
      "Do you want to create your matrix or generate a random one?\n",
      " \n",
      "1 - My own matix\n",
      "2 - Random matix\n",
      "\n",
      " What is your choice? \n",
      " 2\n",
      "\n",
      "matrix:\n",
      " [[26 82 14]\n",
      " [26  1 72]\n",
      " [89 77 91]]\n",
      "----------\n",
      "calculator:\n",
      " {'mean': [[47.0, 53.333333333333336, 59.0], [40.666666666666664, 33.0, 85.66666666666667], 53.111111111111114], 'variance': [[882.0, 1373.5555555555557, 1072.6666666666667], [878.2222222222222, 864.6666666666666, 38.22222222222223], 164115.85185185188], 'standard devitation': [[29.698484809834994, 37.06151043273271, 32.751590292177674], [29.63481436119049, 29.40521495698793, 6.18241233033047], 9.886438927455185], 'max': [[89, 82, 91], [82, 72, 91], 91], 'min': [[26, 1, 14], [14, 1, 77], 1], 'sum': [[141, 160, 177], [122, 99, 257], 956]}\n"
     ]
    }
   ],
   "source": [
    "matrix = init()\n",
    "matrix, dictionary = calculate(matrix)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
