-- love game!! main stuff
A = 0
B = 0
local input_channel
local cookie
local canvas
local width, height
local scale = 1

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
        B = string.gsub(line, "set_cookies", "")
        print("given cookie: ", B)
        io.stdout:flush()
    elseif string.find(line, "set_scale") then
        scale = string.gsub(line, "set_scale", "")
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


function love.load()
    print("Love game has begun")
    io.stdout:flush() -- send message immediately

    canvas = love.graphics.newCanvas(1200, 600)
    width, height = love.graphics.getDimensions()

    cookie = love.graphics.newImage("assets/cookie1.png")
    cookie:setFilter("linear", "nearest")
    
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

function love.mousepressed(x, y, button, isTouch, presses)
    if button == 1 then
        print("add_cookie")
        io.stdout:flush()
        print("get_scale")
        io.stdout:flush()
    elseif button == 2 then
        print("add_friend")
        io.stdout:flush()
    elseif button == 3 then
        print("mid baby bitch boy mouse clicked")
        io.stdout:flush()
    end
end


function love.draw()
    love.graphics.print(A, 20, 20)
    love.graphics.print(B, 20, 40)
    love.graphics.clear(0.04, 0.7, 1, 1)
    love.graphics.push()
    -- love.graphics.translate(-cookie:getWidth(), -cookie:getHeight())
    -- love.graphics.scale(1.6)
    love.graphics.draw(cookie, width/2 -scale*cookie:getWidth()/2, height/2 -scale*cookie:getHeight()/2, 0, scale, scale)
    love.graphics.pop()
end

function get_value()

end


function draw_mech()

end

function draw_shape()

end

function draw_blaster()

end

