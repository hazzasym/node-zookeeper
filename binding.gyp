{
    'variables': {
        'platform': '<(OS)',
    },
    "targets": [{
        "target_name": "zookeeper",
        "sources": ["src/node-zk.cpp"],
        'cflags': ['-Wall', '-O0'],
        'conditions': [
            ['OS=="solaris"', {
                'cflags': ['-Wno-strict-aliasing'],
                'defines': ['_POSIX_PTHREAD_SEMANTICS'],
                'include_dirs': [
                    '/opt/local/include/zookeeper',
                    '<!(node -e "require(\'nan\')")'
                ],
	            'ldflags': ['-lzookeeper_st'],
            }],
            ['OS=="freebsd"', {
                'cflags': ['-I/usr/local/include', '-I/usr/local/include/zookeeper'],
                'include_dirs': [
                    '/usr/local/include/zookeeper',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['/usr/local/lib/libzookeeper_st.a'],
            }],
            ['OS=="mac"',{
                'include_dirs': [
                    '<(module_root_dir)/deps/zookeeper/src/c/include',
                    '<(module_root_dir)/deps/zookeeper/src/c/generated',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['<(module_root_dir)/deps/zookeeper/src/c/.libs/libzookeeper_st.a'],
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                    'MACOSX_DEPLOYMENT_TARGET': '10.5'
                }
            }],['OS=="linux"',{
                'include_dirs': [
                    '<(module_root_dir)/deps/zookeeper/src/c/include',
                    '<(module_root_dir)/deps/zookeeper/src/c/generated',
                    '<!(node -e "require(\'nan\')")'
                ],
                'libraries': ['<(module_root_dir)/deps/zookeeper/src/c/.libs/libzookeeper_st.a'],
            }]
        ]},
        {
            "target_name": "after_build",
            "type": "none",
            "dependencies": ["zookeeper"],
            "actions": [{
                "action_name": "symlink",
                "inputs": ["<@(PRODUCT_DIR)/zookeeper.node"],
                "outputs": ["<(module_root_dir)/build/zookeeper.node"],
                "action": ["sh", "scripts/symlink.sh", "<@(_inputs)"]
            }]
    }],
}
