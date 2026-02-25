;Evaluate expression via py-call:
(= (py-eval $str)
   (let $dict (py-call (dict))
        (py-call (quote (eval $str $dict $dict)))))

;Add to builtins a function that can call functions via keyword arguments
!(py-eval "setattr(__import__('builtins'),'apply_kwargs',(lambda f,d: f(**d))) or 0")

!(py-eval "setattr(__import__('builtins'),'apply_args',(lambda f,args: f(*args))) or 0")

!(let*
    (
        ($numpy (py-call (importlib.import_module "numpy")))
        ($np-random (py-call (getattr $numpy "random")))
        ($rand (py-call (getattr $np-random "dirichlet")))
    )
    (py-call (builtins.apply_args $rand ((1 1) 8)))
)
