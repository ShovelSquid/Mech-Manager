-- love game!! main stuff


Handlers = {
    "get_player_position",
    "get_time",
    "give_cookie"
}

function Handle_Thread_Input(line)
    if line == "get_player_position" then
        Get_player_position()
    elseif line == "get_time" then
        print("get_time", A)
        io.stdout:flush()
        love.handlers["get_time"] = nil
    elseif string.find(line, "set_cookies") then
        local cookie = string.gsub(line, "set_cookies", "")
        B = cookie
        print("given cookie: ", B)
        io.stdout:flush()
    else
        print(line)
        io.stdout:flush()
    end
end

function Get_player_position()
    local x, y = love.mouse.getPosition()
    print(string.format("position: %f, %f", x, y))
    io.stdout:flush() -- flush after every print to prevent hanging
    love.handlers["get_player_position"] = nil
end

A = 0
B = 0
local input_channel

function love.load()
    print("Love game has begun")
    io.stdout:flush() -- send message immediately
    
    -- Create a channel for thread communication
    input_channel = love.thread.getChannel("stdin_input")
    
    -- Create and start stdin reader thread
    local thread_code = [[
        local channel = love.thread.getChannel("stdin_input")
        while true do
            local line = io.stdin:read("*l")
            if line then
                channel:push(line)
            end
        end
    ]]

    local thread = love.thread.newThread(thread_code)
    thread:start()
end

if not love.handlers then
    love.handlers = {}
end

function love.update()
    -- Check for input from the stdin thread (non-blocking)
    local line = input_channel:pop()
    if line then
        love.handlers[line] = true
        Handle_Thread_Input(line)
    end

    -- process queued commands
    -- if love.handlers["get_player_position"] then
    --     --game logic here to get data
    --     Get_player_position()
    -- end
    A = love.timer.getTime()

    -- if love.handlers["get_time"] then
    --     A = love.timer.getTime()
    --     print(A)
    --     io.stdout:flush()
    --     love.handlers["get_time"] = nil
    -- end
end

function love.draw()
    love.graphics.print(A, 20, 20)
    love.graphics.print(B, 20, 40)
end



function draw_mech()

end

function draw_shape()

end

function draw_blaster()

end

