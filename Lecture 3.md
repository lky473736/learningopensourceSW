# Markdown (Markup lang) practice
#### GCU-AI/SW : 오픈소스SW : topic3

markdown file (.md) -> markdown app (.md를 HTML로 변환) -> rendered output

---------------

# Heading level 1 
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
####### Heading level 7?

------------------

## Paragraphs (문단)
statement 1

statement 2 

-------------------

## Line Breaks (줄바꿈)
줄바꿈 할 때 statement 뒤에 공백 2칸 이상 필요

this is the first line  
this is the second line  

------------------

## Emphasis (강조)

### bold
볼드체할 단어 양 끝에 **
I can do **bold**

### italic
이텔릭체할 단어 양 끝에 *
I can do *italic*

### bold and italic
볼드 + 이텔릭체할 단어 양 끝에 ***
I can do ***bold, also italic***

**detail)** \* 그대로 표현하고 싶을 땐 이스케이프 코드 형식으로 사용 (back-slash + \*)

-------

## Blockquotes (인용)
부등호 사용 후 write statement

> hello
> I'm Blockquotes - Lim

-------

## List 
1.
2.
3.

or 

-
-
-

---

## Links

링크를 걸고 싶은 단어를 대괄호로 묶고, 그 뒤에 소괄호 안에 링크 넣기

[Github](https://github.com/lky473736)

---

## Images

느낌표 넣고 이미지 구분할 이름을 대괄호 안에 넣고 이미지 링크 소괄호에 넣기

![markdown logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1024px-Markdown-mark.svg.png)

---

## Escaping Characters

backslash 앞에 사용

\\
\*
\[]
\#
\-
\!

---

## Shell Commands
\`\`\` 사이에 코드 넣기

```python
import turtle
t = turtle.Turtle()
```
