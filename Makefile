##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## Makefile that build project
##

NAME	= 	pbrain-gomoku-ai

SRC		=	./main.py

# SRC_T	=	./tests.py

# TESTS_NAME	=	./unit_tests.py

CP			=	cp

CHMOD		=	chmod

EXEC_RIGHTS	=	+x

RM			=	rm -rf

all: $(NAME)

$(NAME):
	$(CHMOD) $(EXEC_RIGHTS) $(NAME)

tests_run: all
	$(CP) $(SRC_T) $(TESTS_NAME)
	$(CHMOD) $(EXEC_RIGHTS) $(TESTS_NAME)
#	pytest --cov=process --cov=main $(TESTS_NAME)

clean:
#	$(RM) $(TESTS_NAME)
	$(RM) .coverage
	$(RM) .pytest_cache/

fclean: clean

re: fclean all

.PHONY: all clean fclean re