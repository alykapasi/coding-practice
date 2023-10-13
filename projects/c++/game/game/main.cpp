//
//  main.cpp
//  game
//
//  Created by Aly Kapasi on 10/11/23.
//

#include <iostream>

// SFML libraries
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/Audio.hpp>
#include <SFML/System.hpp>

int main()
{
    // Create Window
    sf::RenderWindow window(sf::VideoMode(600, 600), "Ka Ni Na!");

    // Create a font
    sf::Font font;
    if (!font.loadFromFile("/System/Library/Fonts/Supplemental/Arial.ttf"))
    {
        return EXIT_FAILURE;
    }

    // Create text
    sf::Text text;
    text.setFont(font);
    text.setString("Ka Ni Na!");
    text.setCharacterSize(24);
    text.setFillColor(sf::Color::White);

    // Main loop
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }

        window.clear();
        window.draw(text);
        window.display();
    }

    return EXIT_SUCCESS;
}
