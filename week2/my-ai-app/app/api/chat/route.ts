import OpenAI from 'openai';
import { OpenAIStream, StreamingTextResponse } from 'ai';

const openai = new OpenAI({
    baseURL: "https://appearance-morgan-exhibitions-pill.trycloudflare.com/v1/",
});

export const runtime = 'edge';

export async function POST(req: Request) {
  const { messages } = await req.json();
  console.log(messages);

  const response = await openai.chat.completions.create({
    model: 'TheBloke_MythoMax-L2-13B-GPTQ_gptq-4bit-32g-actorder_True',
    stream: true,
    messages: [
      {
        role: "system",
        content:
          `You are a professional joke teller who has been hired to write a series of short jokes for a new anthology. The jokes should be captivating, imaginative, and thought-provoking. They should explore a variety of themes and topics, from science work and people to animals and food. Each joke should be unique and memorable, with compelling characters and unexpected plot twists.`,
      },
      ...messages,
    ],
  });

  const stream = OpenAIStream(response);
  return new StreamingTextResponse(stream);
}