{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMICG+mq/zn7MwN2ljKTxhh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/192412343simats-dot/machine-learning/blob/main/2.%20Candidate%20elimination.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import copy\n",
        "\n",
        "def initialize_hypotheses(n):\n",
        "    hypotheses = []\n",
        "    specific_hypothesis = ['0'] * n\n",
        "    general_hypothesis = ['?'] * n\n",
        "    hypotheses.append(specific_hypothesis)\n",
        "    hypotheses.append(general_hypothesis)\n",
        "    return hypotheses\n",
        "\n",
        "def candidate_elimination(training_data):\n",
        "    num_attributes = len(training_data[0]) - 1\n",
        "    hypotheses = initialize_hypotheses(num_attributes)\n",
        "    for example in training_data:\n",
        "        if example[-1] == 'Yes':\n",
        "            for i in range(num_attributes):\n",
        "                if hypotheses[0][i] != '0' and hypotheses[0][i] != example[i]:\n",
        "                    hypotheses[0][i] = '?'\n",
        "                for h in hypotheses[1:]:\n",
        "                    if h[i] != '?' and h[i] != example[i]:\n",
        "                        hypotheses.remove(h)\n",
        "        else:\n",
        "            temp_hypotheses = copy.deepcopy(hypotheses)\n",
        "            for h in temp_hypotheses:\n",
        "                if h[:-1] != example[:-1] + ['?']:\n",
        "                    hypotheses.remove(h)\n",
        "                for i in range(num_attributes):\n",
        "                    if example[i] != h[i] and h[i] != '?':\n",
        "                        new_hypothesis = copy.deepcopy(h)\n",
        "                        new_hypothesis[i] = '?'\n",
        "                        if new_hypothesis not in hypotheses:\n",
        "                            hypotheses.append(new_hypothesis)\n",
        "\n",
        "    return hypotheses\n",
        "training_data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],\n",
        "['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "result_hypotheses = candidate_elimination(training_data)\n",
        "print(\"Result Hypotheses:\")\n",
        "for h in result_hypotheses:\n",
        "    print(h)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "crD9CuHhmB4Q",
        "outputId": "bbd475f8-d552-4eaa-9dff-fc8d5bde1495"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result Hypotheses:\n",
            "['?', '0', '0', '0', '0', '0']\n"
          ]
        }
      ]
    }
  ]
}