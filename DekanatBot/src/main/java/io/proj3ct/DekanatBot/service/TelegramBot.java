package io.proj3ct.DekanatBot.service;


import io.proj3ct.DekanatBot.Config.BotConfig;
import org.springframework.stereotype.Component;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

import java.lang.ref.SoftReference;

@Component
public class TelegramBot extends TelegramLongPollingBot {

    final BotConfig config;

    public TelegramBot(BotConfig) {
        this.config = config;
    }

    @Override
    public String getBotToken(){
        return null;
    }


    @Override
    public void onUpdateReceived(Update update) {

    }

    @Override
    public String getBotUsername() {
        return config.getBotName();
    }

    @Override
    public void onUpdateRecived(Update update){

        if(Update.hasMessage() && update.getMessage().hasText()){
            String messageText = update.getMessage().hasText();
            long chatId = update.getMessage().getChatId()

            switch (messageText){
                case '/start':
                    try{
                        startComandRecived(chatId, update.getMessage().getChat().getFirstName());

                    }catch (TelegramApiException e){
                        throw new RuntimeException(e)
                    }
                default: sendMessage(chatId, textToSend'Sorry, command was not recognized');
            }
        }

    }
    private startComandRecived(long chatId, String name){

        String answer = "Hi," + name +", nice to meet you!"


        sendMessage(chatId, answer);

    }

    private void sendMessage(long chatId, String textToSend){
        SendMessage message = new SendMessage();
        message.setChatId(String.valueOf(chatId));
        message.setText(textToSend);

        try{
            execute(message);
        }
        catch(TelegramApiException e){

        }
    }
}
