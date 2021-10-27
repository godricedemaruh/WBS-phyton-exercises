{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "910a991c-c960-46dd-82ee-ef3331fe0646",
   "metadata": {},
   "outputs": [],
   "source": [
    "def intersect(set1, set2):\n",
    "    inter_set = set()\n",
    "    for i in set1:\n",
    "        for j in set2:\n",
    "            if i == j:\n",
    "                inter_set.add(i)\n",
    "    return inter_set"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
