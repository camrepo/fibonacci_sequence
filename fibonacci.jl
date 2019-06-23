function fib(n::Int)
    if n < 2
        return n
    else
        return fib(n-2) + fib(n-1)
    end
end


#  @time fib(40)