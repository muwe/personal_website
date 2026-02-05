import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        description: z.string(),
        pubDate: z.coerce.date(),
        updatedDate: z.coerce.date().optional(),
        heroImage: z.string().optional(),
        tags: z.array(z.string()).default([]),
        // 仅在本地开发环境中展示的文章
        localOnly: z.boolean().optional().default(false),
    }),
});

export const collections = { posts };
