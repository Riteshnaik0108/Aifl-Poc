% Predefined valid user
valid_user(ritesh,'123').
valid_user(tesh,'1234').
valid_user(sh,'12345').

% Start point
start :-
    write('Welcome to login system'),nl,
    login.

% Login logic using repeat
login :-
    repeat,
    write('Enter Username: '),
    read(User),
    write('Enter Password: '),
    read(Password),
    ( valid_user(User,Password) ->
        write('Login Successfull'),nl,!
    ;
        write('Invalid Username or Password'),nl,
        fail
    ).



