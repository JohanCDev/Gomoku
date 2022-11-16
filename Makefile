##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## Makefile that build project
##

NAME	= 	pbrain-gomoku-ai

SRC		=	pbrain-gomoku-ai.py

SRC_T	=	./tests/GomokuTests.py

TESTS_NAME	=	./unit_tests.py

CP			=	cp

MV			=	mv

CHMOD		=	chmod

EXEC_RIGHTS	=	+x

RM			=	rm -rf

all: $(NAME)

$(NAME):
	$(CP) src/$(SRC) ./
	$(MV) $(SRC) $(NAME)
	$(CHMOD) $(EXEC_RIGHTS) $(NAME)

tests_run: all
	$(CP) $(SRC_T) $(TESTS_NAME)
	$(CHMOD) $(EXEC_RIGHTS) $(TESTS_NAME)
	pytest $(TESTS_NAME)

clean:
	$(RM) $(TESTS_NAME)
	$(RM) .coverage
	$(RM) .pytest_cache/

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re