import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
    const posts = await getCollection('posts');
    return rss({
        title: 'Aiven\'s Blog',
        description: 'Thinking and writing.',
        site: context.site,
        items: posts.map((post) => ({
            title: post.data.title,
            pubDate: post.data.pubDate,
            description: post.data.description,
            customData: post.data.tags.length > 0 ? post.data.tags.map(tag => `<category>${tag}</category>`).join('') : '',
            link: `/posts/${post.slug}/`,
        })),
    });
}
