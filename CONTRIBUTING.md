# Contributing to PyHP++#

There are two different ways you might want to contribute to PyHP++#:

1. Contribute to the specification.
2. Contribute to the compiled interpreter-compiler, which runs and compiles PyHP++# code.

The process for contributing to the two is different.

## Contributing to the specification

### With a fully-formed spec

If you have a fully-formed spec (a 'Proposal') with defined grammar, semantics, examples, etc, fork the repo, create a branch for your feature off of `master`, add your spec (in Markdown format) to `spec/`, and submit a pull request. The community will look at your idea, and discuss for a while. Eventually, we'll decide whether to accept your idea. If we do, it'll be merged into `master` for all to see.

If your specification is based on a Suggestion, mention the issue ID in your PR's description, like this:

```markdown
# Undefined behavior causes nasal demons

This PR implements #14.

I've created a formal specification that requires undefined behavior to have some chance of causing demons to fly out of the programmer's nose.
```

### With a partially-formed idea

If you have an idea of what you want, but not a formal specification (a 'Suggestion'), submit an issue on the main repo. Everyone will look at it, and discuss for a bit. Eventually, someone might come up with a formal spec to implement it and submit a pull request.

## Contributing to the CIC

If you want to contribute to the compiled interpreter-compiler, you can do so by fixing a bug, adding a CIC feature, or implementing part of the spec that's not yet implemented.

In any case, once you've decided what you want to do, fork the repo, create a new branch off of `master`, and start implementing your code. Make sure to commit regularly, and keep each commit relatively small.

Once you're done implementing, submit a PR, and we'll review it. Once the review process is done, we'll decide whether to merge your PR into `master`.
